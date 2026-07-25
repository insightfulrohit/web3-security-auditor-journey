#!/usr/bin/env python3
"""
arxiv_downloader.py
Search arXiv for a topic and download up to `limit` unique PDF papers.
"""

import os
import time
import re
import requests
import feedparser
import tkinter as tk
from tkinter import filedialog

ARXIV_API = "http://export.arxiv.org/api/query"

def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Choose folder to save research papers")
    root.destroy()
    return folder

def slugify(s, maxlen=120):
    # make a safe filename from title
    s = s.strip().replace("\n", " ")
    s = re.sub(r'[\\/:"*?<>|]+', "", s)              # banned chars
    s = re.sub(r'\s+', ' ', s)
    s = s[:maxlen].strip()
    return s

def download_file(url, dest_path, timeout=30):
    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def search_and_download(topic, folder, limit=20, batch_size=25, wait_seconds=3):
    print(f"Topic: {topic}")
    downloaded = 0
    start = 0
    seen_ids = set()

    os.makedirs(folder, exist_ok=True)

    while downloaded < limit:
        q = f"search_query=all:{requests.utils.quote(topic)}&start={start}&max_results={batch_size}"
        url = f"{ARXIV_API}?{q}"
        print(f"\nQuerying arXiv: start={start}, batch={batch_size} ...")
        feed = feedparser.parse(url)

        if not feed.entries:
            print("No more entries returned by arXiv. Stopping.")
            break

        new_found = False
        for entry in feed.entries:
            # arXiv id: look at entry.id (like http://arxiv.org/abs/XXXX)
            try:
                entry_id_full = entry.get("id", "")
                if not entry_id_full:
                    continue
                arxiv_id = entry_id_full.rsplit("/", 1)[-1]
                if arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)
                new_found = True

                title = entry.get("title", "untitled")
                filename = slugify(f"{arxiv_id} - {title}") + ".pdf"
                filepath = os.path.join(folder, filename)

                if os.path.exists(filepath):
                    print(f"[SKIP] already exists: {filename}")
                    downloaded += 1  # if you prefer not to count existing files, remove this line
                    if downloaded >= limit:
                        break
                    continue

                # Build canonical PDF URL
                pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

                print(f"[{downloaded+1}/{limit}] Downloading {arxiv_id} — {title[:80]} ...")
                try:
                    download_file(pdf_url, filepath)
                    downloaded += 1
                    print(f" Saved -> {filepath}")
                except Exception as e:
                    print(f"  Failed to download {arxiv_id}: {e}")
                    # remove partial file if created
                    if os.path.exists(filepath):
                        try:
                            os.remove(filepath)
                        except:
                            pass

                if downloaded >= limit:
                    break

                time.sleep(1)  # small pause between downloads

            except Exception as e:
                print("  Error processing entry:", e)
                continue

        if not new_found:
            print("No new unique entries in this batch; stopping.")
            break

        start += batch_size
        print(f"Waiting {wait_seconds}s before next query to be polite...")
        time.sleep(wait_seconds)

    print(f"\nDone. Total downloaded (counted): {downloaded}")

def main():
    topic = input("Enter research topic (e.g. 'web application security'): ").strip()
    if not topic:
        print("No topic entered. Exiting.")
        return

    print("Choose folder to save downloaded research papers...")
    folder = choose_folder()
    if not folder:
        print("No folder selected. Exiting.")
        return

    try:
        search_and_download(topic, folder, limit=20)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()

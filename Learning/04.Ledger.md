### **Ledger — Explanation**

This document explains the concept of a ledger in distributed systems.

**Table of Contents**

**1.What is a Ledger?**

**2.Ledger vs. Database**

**3.Types of Ledgers**

**4.Core Components of a Blockchain Ledger**

**5.Key Properties of Ledgers**

### **1. What is a Ledger?**

A ledger is a record-keeping system that stores the history of events (usually transactions) in a structured, auditable form. In the context of distributed systems and blockchain, a ledger is often:

**Append-only:** New entries are added but historical entries are not removed or modified.

**Ordered:** Entries are arranged in a well-defined order (typically by time or block height).

**Verifiable:** Each entry can be verified cryptographically or by consensus.

### **In sorts**
A ledger in blockchain is the canonical, append‑only record of all validated transactions and state changes. The ledger is maintained in a distributed manner across nodes: every full node stores (or[...]


### **2. Ledger vs. Database**

Although both store data, a ledger differs from a typical database in several ways:

**Mutability:** Databases allow inserts, updates, deletes; ledgers are append-only (immutable history).

**Trust model:** Databases usually have a central authority controlling writes/reads; ledgers are often distributed and use consensus to agree on writes.

**Auditability:** Ledgers are designed for tamper-evidence and easy historical audit.

**Replication & Consensus:** Ledgers often include replication across many nodes and a consensus mechanism to accept new entries.

Use a ledger when you need an immutable, auditable, distributed record of events. Use a database when you need fast, mutable, queryable storage for general application data.

### **3. Types of Ledgers**

**(A)Centralized Ledger:** Single authority (traditional bank ledger). Easy to change, trust on the operator.

**(B)Distributed Ledger (DLT):** Copies of ledger are stored across multiple nodes (e.g., HLF, Corda). **Consensus** is used to synchronize state.

**(C)Blockchain (a subset of DLT):** Ledger organized into blocks that reference previous blocks cryptographically (e.g., Bitcoin, Ethereum).

**(D)Permissionless vs Permissioned:**

  **Permissionless:** Anyone can join, read and write (e.g., Bitcoin, public Ethereum).

  **Permissioned:** Only authorized participants can read/write (e.g., Hyperledger Fabric, Corda).

### **4. Core Components of a Blockchain Ledger**

**Transactions** — atomic operations representing state changes (e.g., transfer 5 tokens from A to B).

**Blocks** — batches of transactions with metadata (timestamp, previous block hash, merkle root, nonce (if PoW), etc.).

**Hashes** — cryptographic digests linking blocks and ensuring immutability.

**Merkle Tree / Merkle Root** — compact commitment to the set of transactions in a block enabling efficient proofs.

**Block Header** — contains block metadata used to link and validate blocks.

**State** — current snapshot of accounts, UTXO set, or contract storage derived from processing transactions.

**Chain Height / Block Number** — the position of a block in the chain.

**Event Logs / Indexes** — auxiliary structures for quick queries (transaction index, address index).

### **5. Key Properties of Ledgers**

**Immutability / Tamper-evidence:** Past entries are cryptographically linked; altering history breaks hashes.

**Decentralization / Fault Tolerance:** Replication across nodes increases resilience to single-point failures.

**Transparency & Auditability:** Anyone (or authorized parties) can verify ledger contents.

**Consensus & Agreement:** Nodes must agree on the sequence of entries.

**Availability:** Nodes generally keep copies to serve read requests.

**Trade-offs exist:** high decentralization may reduce throughput and increase latency; permissioned ledgers trade openness for performance.

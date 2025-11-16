# Working of Blockchain (Step-by-Step With Example)

This document explains how a blockchain processes a transaction in a very simple, easy-to-understand flow.  
Arrows show the exact direction of the process.

---

## Step-by-Step Working

Ask for a Transaction  
⬇️  
A user creates a transaction (example: sending 2 BTC to a friend)  
⬇️  
The wallet **signs** the transaction using the user’s private key  
⬇️  
The signed transaction is **broadcast** to the blockchain network  
⬇️  
All connected **nodes receive** the transaction request  
⬇️  
Nodes perform basic checks (balance, signature, format, previous history) 
⬇️  
If valid, the transaction is placed into the **mempool** (waiting area)  
⬇️
Miners/Validators pick this and other transactions from the mempool  
⬇️
They create a **new candidate block** containing these transactions  
⬇️
Consensus happens  
- In **Proof of Work**, miners solve a puzzle  
- In **Proof of Stake**, validators are selected to approve the block  
⬇️
The block that wins consensus is **broadcast** to the entire network  
⬇️
Nodes verify the new block and add it to their local blockchain copy  
⬇️
The transaction becomes part of the chain  
⬇️
Other blocks get added on top → giving **confirmations**  
⬇️
Once enough confirmations are received →  
**The transaction is considered final!**

---

## Simple Example

Let’s say **Alice wants to send 2 BTC to Bob**.

1. Alice enters Bob’s address and amount in her wallet.  
2. Wallet signs the transaction with Alice’s private key.  
3. Transaction spreads across the Bitcoin network.  
4. Nodes check:  
   - “Does Alice really have 2 BTC?”  
   - “Is the signature valid?”  
5. Valid transaction sits in the mempool.  
6. Miners pick it and put it into a block (along with many others).  
7. Miner solves the PoW puzzle → publishes the block.  
8. Other nodes verify it → block becomes part of the chain.  
9. After 6 confirmations, the network agrees it is final.

**Bob now officially owns 2 BTC.**

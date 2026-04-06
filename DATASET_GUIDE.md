#  Dataset Guide

##  Neuro-Symbolic AI for Automated Cyber Threat Intelligence

---

##  1. Why Datasets Matter in This Project

In this project, datasets are the **foundation of intelligence**.

 The system learns:

* What normal network behavior looks like
* What attack patterns look like
* How attackers behave in real-world scenarios

Without good datasets → no learning,  no detection

---

##  2. Datasets Used in This Project

We use **three major cybersecurity datasets**:

### 🔹 1. CICIDS2017

* Realistic network traffic dataset
* Contains both **normal and attack traffic**
* Used for:

  * Intrusion detection
  * Anomaly detection

 Helps the model understand real-world attack scenarios

---

### 🔹 2. BoT-IoT Dataset

* Focuses on **IoT-based attacks**
* Includes:

  * Botnet activity
  * DDoS attacks
  * Data exfiltration

 Useful for detecting large-scale automated attacks

---

### 🔹 3. TON_IoT Dataset

* Designed for **smart environments and IoT systems**
* Contains:

  * Network traffic
  * System logs
  * Attack labels

 Used mainly for:

* Graph construction
* Trust modeling

---

##  3. How Data is Represented

### 🔹 3.1 Graph-Based Representation

Instead of treating data as rows, we convert it into a **graph**:

```
G = (V, E)
```

Where:

* V → Nodes (IP addresses, devices, users)
* E → Edges (connections between them)

 Why this is powerful:

* Cyber attacks spread across networks
* Graphs capture relationships and attack paths

---

##  4. Types of Data Features

Each data record contains multiple types of features:

### 🔸 1. Basic Network Features

* Duration of connection
* Protocol type (TCP, UDP, ICMP)
* Service used (HTTP, FTP, etc.)

 Helps identify general traffic behavior

---

### 🔸 2. Traffic Features

* Number of connections
* Error rates
* Service usage patterns

 Helps detect abnormal spikes (e.g., DDoS attacks)

---

### 🔸 3. Content Features

* Login attempts
* File access
* Root access

 Helps detect insider attacks or privilege misuse

---

### 🔸 4. Host-Based Features

* Activity of a specific IP/device
* Connection patterns over time

 Helps detect scanning or probing attacks

---

##  5. Data Preprocessing (Very Important Step)

Before feeding data into models, we clean and transform it:

### ✔ Steps:

1. Remove unnecessary columns
2. Handle missing values
3. Convert categorical → numerical (encoding)
4. Normalize data (scaling)

 Result: Clean, structured data ready for AI models

---

##  6. Graph Construction (TON_IoT)

From TON_IoT dataset:

* Each **IP address → Node**
* Each **connection → Edge**

We also calculate:

* Number of connections (degree)
* Attack ratio of each node

 This helps the model understand:

* Which nodes are trusted
* Which nodes are suspicious

---

##  7. How Each Model Uses the Data

### 🔹 Transformer Model

* Uses **tabular + sequential data**
* Learns:

  * Time-based attack patterns
  * Multi-step attacks

---

### 🔹 GNN Model

* Uses **graph data**
* Learns:

  * Relationships between nodes
  * Trust levels of entities

---

### 🔹 Symbolic AI

* Uses **rules + model outputs**
* Converts predictions into:

  * Human-readable explanations

---

##  8. Labels in Dataset

Each data point is labeled as:

* 0 → Normal
* 1 → Attack

 This helps models learn:

* Classification (normal vs malicious)

---

## 📊 9. Data Challenges (Real-World Issues)

Working with cybersecurity datasets is not easy:

###  Common Problems:

* Imbalanced data (more normal than attacks)
* Noisy or missing values
* New unseen attacks (Zero-Day)

 Solution used in project:

* Advanced models (Transformer + GNN)
* Adversarial training
* Graph-based learning

---

##  10. Why These Datasets Are Powerful

These datasets are widely used in research because they:

* Simulate real-world cyber attacks
* Include multiple attack types
* Support both:

  * Deep learning
  * Graph-based learning

 As mentioned in the research, they are essential for evaluating modern cybersecurity models 

---

##  11. Complete Data Flow

```
Raw Dataset
→ Data Cleaning
→ Feature Extraction
→ Graph Construction
→ Transformer Input
→ GNN Input
→ Symbolic Reasoning
→ Final Output
```

---

##  Final Understanding

 In simple words:

* Dataset = “experience” of the system
* More diverse data = smarter model

This project uses powerful datasets to build a system that:

* Detects attacks
* Understands behavior
* Explains decisions

---

##  Final Line

A strong dataset is not just data —
it is the **intelligence behind your cybersecurity system**.

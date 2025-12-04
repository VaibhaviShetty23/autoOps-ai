# AutoOps AI – Enterprise Incident Response Agent


<img width="500" height="500" alt="autoops" src="https://github.com/user-attachments/assets/b0ec3757-9c88-4a84-868d-8be994e7f332" />

**Track:** Enterprise Agents  
**Course:** 5-Day AI Agents Intensive Course with Google (Nov 10-14, 2025)  
**Author:** Vaibhavi Shetty  
**GitHub:** https://github.com/VaibhaviShetty23/autoOps-ai  

---

## Overview

AutoOps AI is an **Enterprise AI agent system** designed to automatically investigate operational incidents in cloud applications, analyze logs and metrics, identify root causes, and propose actionable fixes. It leverages **Gemini LLM** as the reasoning engine and demonstrates a **multi-agent architecture**.

This project serves as a **Minimum Viable Product (MVP)** for the Kaggle AI Agents Capstone.

---

## Features Demonstrated

The project applies **at least three key concepts** from the course:

1. **Multi-agent system**  
   - `LogAgent` → parses logs  
   - `MetricsAgent` → analyzes metrics  
   - `RootCauseAgent` → identifies root cause using Gemini LLM  
   - `FixAgent` → proposes fix using Gemini LLM  
   - `ReportAgent` → compiles a structured incident report  

2. **Tools & LLM Integration**  
   - Gemini LLM powers root cause analysis, fix recommendation, and evaluation.  
   - Configured via `.env` with API key.  

3. **Sessions & Context Management**  
   - `Coordinator` tracks a `trace_id` across all agents to maintain context.  

4. **Optional Evaluation (Bonus)**  
   - LLM-as-Judge evaluates accuracy, clarity, and usefulness of the report.  

---

## Architecture

```text
+------------------+
|   Coordinator    |
+--------+---------+
         |
         v
+--------+---------+       +----------------+
| LogAgent          |      | MetricsAgent   |
| (parse logs)      |      | (analyze)      |
+--------+---------+       +--------+-------+
         |                          |
         v                          v
      RootCauseAgent  (Gemini LLM) ---> FixAgent (Gemini LLM)
                                     |
                                     v
                                ReportAgent
```

**Coordinator**: Orchestrates workflow, manages trace IDs

**Agents**: Each agent performs a specialized task

**Gemini LLM**: Powers reasoning for root cause and fix recommendation

---

## Installation

1. **Clone the repository:**

```
git clone <repo-url>
cd autoops-ai
```
2. **Install dependencies:**
```
pip install -r requirements.txt
```
3. **Set your Gemini API key in .env:**
```
GEN_API_KEY=<your_api_key>
```

---

## Usage

1. **Run the main application:**
```
python app.py
```

2. **Example input:**
```
Describe the incident: App returns 502 Bad Gateway after a new deployment.
```


3. **Sample output:**
```
=== AUTOOPS AI REPORT ===
Incident: App returns 502 Bad Gateway after a new deployment.
Logs: ERROR 503 at payment-service | Timeout to DB
Metrics: Latency spike detected between 3PM–3:10PM
Root Cause: A recent deployment introduced a database performance regression in payment-service.
Fix Recommendation: Rollback the deployment or optimize DB queries.
```

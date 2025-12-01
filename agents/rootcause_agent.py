from llm.gemini_client import call_gemini

def analyze_root_cause(logs, metrics, history):
    prompt = f"""
You are an SRE AI Agent.

Analyze the incident and detect root cause using logs, metrics and history.

Logs:
{logs}

Metrics:
{metrics}

History:
{history}

Give ONE root cause with explanation.
"""

    root_cause = call_gemini(prompt)
    return root_cause, history 
# # agents/rootcause_agent.py
# from observability.logger import log
# from tools.incident_search import search_history
# from llm.gemini_client import generate as gemini_generate

# def run(logs, metrics, trace_id, use_gemini=True):
#     history = search_history()
#     log("RootCauseAgent", f"[{trace_id}] Searching history")
#     # Compose a focused prompt
#     prompt = f"""
# You are an incident analysis assistant.
# Given logs:
# {logs}

# And metrics summary:
# {metrics}

# And historical note:
# {history}

# Identify the most likely root cause in one short sentence and include a short rationale.
# """
#     if use_gemini:
#         response = gemini_generate(prompt, max_tokens=200, temperature=0.0)
#     else:
#         response = "Database connection pool exhausted (mock)"
#     # The response may include cause + rationale. For the MVP, we extract first sentence as cause.
#     cause = response.split("\n")[0].strip()
#     log("RootCauseAgent", f"[{trace_id}] Root cause identified: {cause}")
#     return cause, history

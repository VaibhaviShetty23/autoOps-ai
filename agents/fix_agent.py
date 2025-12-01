from llm.gemini_client import call_gemini

def propose_fix(root_cause, trace_id=None):
    prompt = f"""
You are a Senior Platform Engineer.

Given the root cause below, propose actionable remediation steps.

Root cause:
{root_cause}

Return a production-ready fix plan.
"""

    return call_gemini(prompt)


# # agents/fix_agent.py
# from observability.logger import log
# from llm.gemini_client import generate as gemini_generate

# def run(cause, trace_id, use_gemini=True):
#     prompt = f"""
# You are a remediation assistant.
# Root cause: {cause}

# Provide a concise recommended fix plan (one to three actions) and a short rationale.
# """
#     if use_gemini:
#         fix = gemini_generate(prompt, max_tokens=120, temperature=0.0)
#     else:
#         fix = "Increase DB pool size and restart service (mock)"
#     fix = fix.strip()
#     log("FixAgent", f"[{trace_id}] Proposed fix: {fix}")
#     return fix

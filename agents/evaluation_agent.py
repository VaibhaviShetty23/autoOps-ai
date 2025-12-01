from llm.gemini_client import call_gemini
import json
import re

def evaluate_report(incident, report):
    prompt = f"""
You are QA Lead AI.

Evaluate report below on accuracy, clarity and usefulness from 1 to 10.
Return STRICT JSON only.

Incident:
{incident}

Report:
{report}

Format:
{{ "accuracy": X, "clarity": X, "usefulness": X }}
"""

    text = call_gemini(prompt)
    numbers = re.findall(r'\d+', text)

    return {
        "accuracy": numbers[0],
        "clarity": numbers[1],
        "usefulness": numbers[2],
    }

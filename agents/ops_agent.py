import os
from dotenv import load_dotenv
import google.generativeai as genai
from agents.decision_agent import route_decision
from tools.incident_logger import log_incident

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

def process_request(user_input):
    prompt = f"""
You are an Enterprise DevOps AI Agent.

Analyze the issue below.
Detect root cause.
Suggest fix.
Decide severity level.

Issue:
{user_input}
"""

    response = model.generate_content(prompt).text
    next_step = route_decision(response)
    log_incident(user_input, response, next_step)

    return f"{response}\n\nNext Action: {next_step}"

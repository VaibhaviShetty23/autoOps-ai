from datetime import datetime

def log_incident(issue, response, action):
    with open("incidents.log", "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"Issue: {issue}\n")
        f.write(f"Analysis: {response}\n")
        f.write(f"Action: {action}\n")

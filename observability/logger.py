import datetime

def log(agent, message):
    ts = datetime.datetime.now().isoformat()
    print(f"[{ts}] [{agent}] {message}")

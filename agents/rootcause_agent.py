from observability.logger import log
from tools.incident_search import search_history

def run(logs, metrics, trace_id):
    history = search_history()
    cause = "Database connection pool exhausted"
    log("RootCauseAgent", f"[{trace_id}] Root cause identified")
    return cause, history

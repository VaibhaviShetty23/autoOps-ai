from observability.logger import log

def run(cause, trace_id):
    fix = "Increase DB pool size and restart service"
    log("FixAgent", f"[{trace_id}] Proposed fix")
    return fix

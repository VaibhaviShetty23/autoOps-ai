from observability.logger import log
from tools.log_parser import parse_logs

def run(trace_id):
    logs = parse_logs()
    log("LogAgent", f"[{trace_id}] Parsed logs")
    return logs

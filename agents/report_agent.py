from observability.logger import log

def run(incident, logs, metrics, cause, fix, trace_id):
    log("ReportAgent", f"[{trace_id}] Generated report")
    return f"""
INCIDENT REPORT

Incident: {incident}

Logs: {logs}
Metrics: {metrics}

Root Cause: {cause}

Fix Recommendation:
{fix}
"""

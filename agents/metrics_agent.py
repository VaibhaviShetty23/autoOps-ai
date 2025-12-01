from observability.logger import log
from tools.anomaly_detector import detect_anomaly

def run(trace_id):
    metrics = detect_anomaly()
    log("MetricsAgent", f"[{trace_id}] Analyzed metrics")
    return metrics

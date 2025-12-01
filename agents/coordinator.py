from observability.logger import log
from observability.tracing import trace

from agents.log_agent import run as log_agent
from agents.metrics_agent import run as metrics_agent
from agents.rootcause_agent import analyze_root_cause as root_agent
from agents.fix_agent import propose_fix as fix_agent
from agents.report_agent import run as report_agent

from memory.memory_bank import MemoryBank
from evaluation.judge import score

import os
USE_GEMINI = os.environ.get("USE_GEMINI", "1") not in ("0", "false", "False")

class Coordinator:
    def __init__(self):
        self.memory = MemoryBank()

    def investigate(self, incident):
        trace_id = trace()
        log("Coordinator", f"[{trace_id}] New incident received")

        recall = self.memory.recall(incident)
        if recall:
            log("Coordinator", f"[{trace_id}] Found similar past incident")

        logs = log_agent(trace_id)
        metrics = metrics_agent(trace_id)

        # cause, history = root_agent(logs, metrics, trace_id)
        # fix = fix_agent(cause, trace_id)
        
        cause, history = root_agent(logs, metrics, trace_id)
        fix = fix_agent(cause, trace_id)

        self.memory.save(incident, cause, fix)

        report = report_agent(incident, logs, metrics, cause, fix, trace_id)
        scores = score()

        return report, scores
  
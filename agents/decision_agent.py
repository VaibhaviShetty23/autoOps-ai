def route_decision(agent_output):
    if "critical" in agent_output.lower():
        return "Escalate to SRE Team"
    elif "restart" in agent_output.lower():
        return "Restart Service"
    elif "timeout" in agent_output.lower():
        return "Check Load Balancer"
    else:
        return "Log & Monitor"

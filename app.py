from agents.coordinator import Coordinator
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    system = Coordinator()

    incident = input("Describe the incident: ")

    report, scores = system.investigate(incident)

    print("\n=== AUTOOPS AI REPORT ===")
    print(report)

    print("\n=== EVALUATION (LLM-as-Judge) ===")
    for k,v in scores.items():
        print(f"{k}: {v}/10")

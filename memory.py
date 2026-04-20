# memory.py

def store_execution(goal: str, plan: list, results: dict) -> dict:
    memory = {
        "goal": goal,
        "plan": plan,
        "results": results
    }
    return memory
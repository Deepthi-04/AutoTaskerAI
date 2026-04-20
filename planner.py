# planner.py

def create_plan(user_goal: str) -> list:
    goal = user_goal.lower()
    plan = []

    if "summarize" in goal or "summary" in goal:
        plan.append("summarize_text")

    if "insight" in goal or "key point" in goal or "important point" in goal:
        plan.append("extract_insights")

    if "quiz" in goal or "question" in goal:
        plan.append("generate_quiz")

    return plan
# executor.py

from tools import summarize_text, extract_insights, generate_quiz
from memory import store_execution


def execute_plan(goal: str, plan: list, text: str) -> dict:
    results = {}

    for task in plan:
        if task == "summarize_text":
            results["summarize_text"] = summarize_text(text)

        elif task == "extract_insights":
            results["extract_insights"] = extract_insights(text)

        elif task == "generate_quiz":
            results["generate_quiz"] = generate_quiz(text)

    memory = store_execution(goal, plan, results)
    return memory
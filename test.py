print("RUNNING FILE")

from planner import create_plan
from executor import execute_plan

print("Step 1: file started")

goal = "Summarize this text and generate quiz questions"

text = """
Artificial Intelligence is transforming industries by automating tasks,
improving decision-making, and enabling new innovations in healthcare,
finance, and technology.
"""

print("Step 2: before create_plan")
plan = create_plan(goal)
print("Step 3: plan created ->", plan)

print("Step 4: before execute_plan")
result = execute_plan(goal, plan, text)
print("Step 5: after execute_plan")

print("\nFinal Output:")
print(result)
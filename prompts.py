# prompts.py

SUMMARY_PROMPT = """
You are an assistant that summarizes text.

Summarize the following content in a clear and concise way.
Keep it short and easy to understand.

Content:
{text}
"""

INSIGHTS_PROMPT = """
You are an assistant that extracts key insights.

From the following content, extract 5 important insights or key points.

Content:
{text}
"""

QUIZ_PROMPT = """
You are an assistant that generates quiz questions.

From the following content, generate 5 quiz questions with answers.

Format:
Q1: question
A1: answer

Content:
{text}
"""
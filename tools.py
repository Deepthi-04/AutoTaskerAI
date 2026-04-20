# tools.py

import ollama
from prompts import SUMMARY_PROMPT, INSIGHTS_PROMPT, QUIZ_PROMPT

MODEL_NAME = "gemma3"


def get_llm_response(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]


def summarize_text(text: str) -> str:
    prompt = SUMMARY_PROMPT.format(text=text)
    return get_llm_response(prompt)


def extract_insights(text: str) -> str:
    prompt = INSIGHTS_PROMPT.format(text=text)
    return get_llm_response(prompt)


def generate_quiz(text: str) -> str:
    prompt = QUIZ_PROMPT.format(text=text)
    return get_llm_response(prompt)
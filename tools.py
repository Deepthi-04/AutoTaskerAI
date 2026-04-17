# tools.py

import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SUMMARY_PROMPT, INSIGHTS_PROMPT, QUIZ_PROMPT

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)


def get_llm_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content


def summarize_text(text: str) -> str:
    prompt = SUMMARY_PROMPT.format(text=text)
    return get_llm_response(prompt)


def extract_insights(text: str) -> str:
    prompt = INSIGHTS_PROMPT.format(text=text)
    return get_llm_response(prompt)


def generate_quiz(text: str) -> str:
    prompt = QUIZ_PROMPT.format(text=text)
    return get_llm_response(prompt)
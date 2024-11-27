import sys
import os
import re

import openai
import dotenv


dotenv.load_dotenv()


TAG_PROMPT = """
You are an instagram expert.

You take a topic from me and suggest 3-5 tags, that
characterize the post in the context of my personal goal, which is to practice a digital art and to study composition, colors etc.
You responsd in a single line text containg only tags (starting with #).
For example:
#art #landscape #winter #workinprogress
"""


def suggest_tags(text: str) -> str:
    cli = openai.OpenAI()
    suggestions_str = (
        cli.chat.completions.create(
            messages=[
                {"role": "system", "content": TAG_PROMPT},
                {"role": "user", "content": f"The text of the post is:\n{text}"},
            ],
            model="gpt-4o-mini",
        )
        .choices[0]
        .message.content
    )
    return str(suggestions_str)


def extract_text(text: str) -> str:
    text_without_images = re.sub("!\[\[.*\]\]", "", text)
    removed_multi_blank_lines = re.sub(r"\n\s*\n", "\n\n", text_without_images)
    return removed_multi_blank_lines


def main():
    if len(sys.argv) < 2:
        print("You have not provided the processed text.")
        exit(1)
    try:
        text = sys.argv[1]
        if os.path.isfile(text):
            with open(text, "r") as f:
                text = f.read()
        text = extract_text(text)
        if len(sys.argv) > 2 and "-t" in sys.argv:
            tags = suggest_tags(text)
            if tags:
                text = tags + "\n" + text

        print("-" * 100)
        print("Extracted text:\n")
        print(text)
        print("\n")
        exit(0)
    except Exception as e:
        print(e)
        exit(1)

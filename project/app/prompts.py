import os

def read_text_file(path):
    with open(path, "r") as f:
        text = f.read()
    return text


BASE_DIR = os.path.join("app", "prompts")


# Legislation Parsing
LEG_PARSE_PROMPT = os.path.join(BASE_DIR, "legislation-parse", "parseV1.txt")
legislation_prompt = read_text_file(LEG_PARSE_PROMPT)
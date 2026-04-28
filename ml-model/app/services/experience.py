import re

def extract_experience(text):
    match = re.search(r'(\d+)\+?\s*(years|year)', text)
    if match:
        return int(match.group(1))
    return 0
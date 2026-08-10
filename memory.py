import json
import os
import re

MEMORY_FILE = "memory/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_memory(memory):
    os.makedirs("memory", exist_ok=True)

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def normalize_text(text):
    """
    Makes two similar sentences easier to compare.
    """

    text = text.lower().strip()

    # Remove question marks and punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Remove common words
    words_to_remove = [
        "my",
        "the",
        "a",
        "an",
        "about",
        "is",
        "are",
        "am",
        "do",
        "you",
        "remember",
        "what",
        "who",
        "where",
        "when",
        "how"
    ]

    words = text.split()

    words = [
        word for word in words
        if word not in words_to_remove
    ]

    return " ".join(words).strip()


def clean_key(key):

    key = key.lower().strip()

    key = key.replace("?", "")

    return key.strip()


def remember(key, value):

    memory = load_memory()

    key = clean_key(key)

    memory[key] = value

    save_memory(memory)

    return f"I'll remember that {key} is {value}."


def recall(key):

    memory = load_memory()

    requested_key = normalize_text(key)

    # Exact normalized match
    for saved_key, value in memory.items():

        saved_normalized = normalize_text(saved_key)

        if requested_key == saved_normalized:

            return f"You told me that {saved_key} is {value}."

    # Partial match
    for saved_key, value in memory.items():

        saved_normalized = normalize_text(saved_key)

        if (
            requested_key in saved_normalized
            or saved_normalized in requested_key
        ):

            return f"You told me that {saved_key} is {value}."

    return f"I don't have anything saved about {key}."


def get_all_memory():

    return load_memory()

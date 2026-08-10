import requests


def ask_friday(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"""
You are Friday, an intelligent AI assistant.
Answer clearly and helpfully.

User:
{prompt}

Friday:
""",
                "stream": False
            }
        )

        data = response.json()

        return data["response"]

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    question = input("Ask Friday: ")
    print("Friday:", ask_friday(question))
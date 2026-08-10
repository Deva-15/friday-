import ollama

def ask_friday(prompt):
    try:
        # System instructions to force Friday to speak in Telugish / Chatting language
        system_instruction = (
            "You are Friday, an AI assistant created for Dev. "
            "Always respond in friendly Telugu-English chatting script (Telugish) "
            "like a close friend speaking casual Telugu written using English alphabet. "
            "Keep your responses short, natural, clear, and easy to understand. "
            "Do not output native Telugu script, only use English alphabet for Telugu words."
        )

        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'system',
                    'content': system_instruction
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"
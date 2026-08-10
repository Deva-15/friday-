from speak import speak
from listen import listen
from apps import open_app

from friday_ai import ask_friday
from memory import remember, recall

from friday_tools import (
    open_google,
    open_youtube,
    search_google,
    search_youtube,
    open_website
)

from mac_control import execute_mac_command


def handle_memory(command):
    """
    Handles natural memory commands.
    """

    # -------------------------
    # REMEMBER
    # -------------------------

    remember_phrases = [
        "remember that",
        "remember my",
        "remember i am",
        "remember i'm",
        "remember i ",
    ]

    for phrase in remember_phrases:

        if command.startswith(phrase):

            information = command[len(phrase):].strip()

            if not information:
                return "What should I remember?"

            # Example:
            # "my favourite subject is cyber security"

            if " is " in information:

                key, value = information.split(" is ", 1)

                key = key.strip()
                value = value.strip()

                return remember(key, value)

            return remember("general", information)

    # -------------------------
    # RECALL / REMEMBER QUESTIONS
    # -------------------------

    recall_phrases = [
        "do you remember",
        "what do you remember about",
        "what is my",
        "what are my",
        "what am i",
        "what i'm",
        "what i am",
    ]

    for phrase in recall_phrases:

        if command.startswith(phrase):

            key = command[len(phrase):].strip()

            # Remove question marks
            key = key.replace("?", "").strip()

            # Remove common words
            words_to_remove = [
                "my ",
                "the ",
                "about "
            ]

            for word in words_to_remove:

                if key.startswith(word):
                    key = key[len(word):].strip()

            if not key:
                return "What would you like me to remember?"

            return recall(key)

    return None


def main():

    speak("Friday online. Ready Dev.")

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower().strip()

        print("🧑 You:", command)

        # -------------------------
        # EXIT
        # -------------------------

        if command in ["exit", "bye", "quit", "stop"]:

            speak("Going offline")
            break

        # -------------------------
        # MEMORY
        # -------------------------

        memory_response = handle_memory(command)

        if memory_response:

            speak(memory_response)
            continue

        # -------------------------
        # GREETINGS
        # -------------------------

        elif "hello" in command or "hi" in command:

            speak("Hello Dev.")

        # -------------------------
        # GOOGLE
        # -------------------------

        elif "open google" in command:

            speak(open_google())

        # -------------------------
        # YOUTUBE
        # -------------------------

        elif "open youtube" in command:

            speak(open_youtube())

        # -------------------------
        # SEARCH YOUTUBE
        # -------------------------

        elif command.startswith("search youtube for"):

            query = command.replace(
                "search youtube for",
                "",
                1
            ).strip()

            if query:
                speak(search_youtube(query))
            else:
                speak("What should I search on YouTube?")

        # -------------------------
        # GOOGLE SEARCH
        # -------------------------

        elif command.startswith("search for"):

            query = command.replace(
                "search for",
                "",
                1
            ).strip()

            if query:
                speak(search_google(query))
            else:
                speak("What should I search?")

        elif command.startswith("search"):

            query = command.replace(
                "search",
                "",
                1
            ).strip()

            if query:
                speak(search_google(query))
            else:
                speak("What should I search?")

        # -------------------------
        # MAC CONTROLS
        # -------------------------

        elif (
            "time" in command
            or "date" in command
            or "today" in command
            or "battery" in command
            or "screenshot" in command
            or "increase volume" in command
            or "decrease volume" in command
        ):

            speak(execute_mac_command(command))

        # -------------------------
        # CLOSE APP
        # -------------------------

        elif command.startswith("close"):

            speak(execute_mac_command(command))

        # -------------------------
        # OPEN APP / WEBSITE
        # -------------------------

        elif command.startswith("open"):

            mac_result = execute_mac_command(command)

            if mac_result != "Command not recognized":

                speak(mac_result)

            else:

                name = command.replace(
                    "open",
                    "",
                    1
                ).strip()

                website_result = open_website(name)

                if website_result:

                    speak(website_result)

                else:

                    speak(open_app(name))

        # -------------------------
        # AI BRAIN
        # -------------------------

        else:

            speak("Let me think.")

            response = ask_friday(command)

            speak(response)


if __name__ == "__main__":
    main()
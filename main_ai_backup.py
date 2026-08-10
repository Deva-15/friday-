from speak import speak
from listen import listen
from apps import open_app

from friday_ai import ask_friday

from friday_tools import (
    open_google,
    open_youtube,
    search_google,
    search_youtube,
    open_website
)

from mac_control import execute_mac_command


def main():

    speak("Friday online. Ready Dev.")

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower().strip()

        print("🧑 You:", command)

        # Exit
        if command in ["exit", "bye", "quit", "stop"]:
            speak("Going offline")
            break

        # Greetings
        elif "hello" in command or "hi" in command:
            speak("Hello Dev.")

        # Open Google
        elif "open google" in command:
            speak(open_google())

        # Open YouTube
        elif "open youtube" in command:
            speak(open_youtube())

        # Search YouTube
        elif command.startswith("search youtube for"):
            query = command.replace("search youtube for", "").strip()

            if query:
                speak(search_youtube(query))
            else:
                speak("What should I search on YouTube?")

        # Google Search
        elif command.startswith("search for"):
            query = command.replace("search for", "").strip()

            if query:
                speak(search_google(query))
            else:
                speak("What should I search?")

        elif command.startswith("search"):
            query = command.replace("search", "").strip()

            if query:
                speak(search_google(query))
            else:
                speak("What should I search?")

        # Time / Date / Battery / Screenshot / Volume
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

        # Close Application
        elif command.startswith("close"):
            speak(execute_mac_command(command))

        # Open App / Website / Folder
        elif command.startswith("open"):

            mac_result = execute_mac_command(command)

            if mac_result != "Command not recognized":
                speak(mac_result)

            else:
                name = command.replace("open", "").strip()

                website_result = open_website(name)

                if website_result:
                    speak(website_result)
                else:
                    speak(open_app(name))

        # AI Brain
        else:
            speak("Let me think.")

            response = ask_friday(command)

            speak(response)


if __name__ == "__main__":
    main()
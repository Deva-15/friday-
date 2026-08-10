from speak import speak
from listen import listen
from apps import open_app

from friday_ai import ask_friday
from memory import remember, recall

from reminders import start_reminder_checker

from friday_tools import (
    open_google,
    open_youtube,
    search_google,
    search_youtube,
    open_website
)

from mac_control import execute_mac_command

from notes import (
    create_note,
    create_quick_note,
    open_notes
)

from whatsapp import handle_whatsapp


# ============================================================
# MEMORY
# ============================================================

def handle_memory(command):

    if command.startswith("remember that"):

        information = command.replace(
            "remember that",
            "",
            1
        ).strip()

        if not information:
            return "What should I remember?"

        if " is " in information:

            key, value = information.split(
                " is ",
                1
            )

            return remember(
                key.strip(),
                value.strip()
            )

        return remember(
            "general",
            information
        )

    if command.startswith("remember my"):

        information = command.replace(
            "remember my",
            "my ",
            1
        ).strip()

        if " is " in information:

            key, value = information.split(
                " is ",
                1
            )

            return remember(
                key.strip(),
                value.strip()
            )

        return remember(
            "general",
            information
        )

    recall_phrases = [
        "do you remember",
        "what do you remember about",
        "what is my",
        "what are my"
    ]

    for phrase in recall_phrases:

        if command.startswith(phrase):

            key = command.replace(
                phrase,
                "",
                1
            ).strip()

            key = key.replace(
                "?",
                ""
            ).strip()

            if key.startswith("my "):
                key = key[3:]

            return recall(key)

    return None


# ============================================================
# NOTES
# ============================================================

def handle_notes(command):

    if command in [
        "open notes",
        "open note"
    ]:

        return open_notes()

    if command in [
        "create a new note",
        "create new note",
        "create a note",
        "new note",
        "make a new note",
        "make a note"
    ]:

        speak("What should I write in the note?")

        note_text = listen()

        if not note_text:
            return "I didn't hear what you wanted me to write."

        print("📝 Note:", note_text)

        return create_quick_note(note_text)

    if command.startswith("write a note"):

        note_text = command.replace(
            "write a note",
            "",
            1
        ).strip()

        if not note_text:

            speak("What should I write?")

            note_text = listen()

        if not note_text:
            return "I didn't hear anything to write."

        return create_quick_note(note_text)

    if command.startswith("take a note"):

        note_text = command.replace(
            "take a note",
            "",
            1
        ).strip()

        if not note_text:

            speak("What should I write?")

            note_text = listen()

        if not note_text:
            return "I didn't hear anything to write."

        return create_quick_note(note_text)

    return None


# ============================================================
# REMINDERS
# ============================================================

def handle_reminder(command):

    if not command.startswith("remind me"):
        return None

    speak(
        "Reminder system is connected. "
        "Please say the reminder time in 24 hour format, "
        "for example 18:00."
    )

    return "Reminder feature is ready."


# ============================================================
# WHATSAPP CHAT COMMAND
# ============================================================

def handle_whatsapp_chat_open(command):

    chat_phrases = [
        "open chat",
        "open the chat",
        "open chat with",
        "open the chat with",
        "open whatsapp chat",
        "open whatsapp chat with",
        "open whatsapp the chat",
        "open whatsapp the chat with"
    ]

    # --------------------------------------------------------
    # "open Amma chat"
    # --------------------------------------------------------

    if command.startswith("open ") and command.endswith(" chat"):

        contact = command[
            len("open "):-len(" chat")
        ].strip()

        if contact:

            return handle_whatsapp(
                f"whatsapp search for {contact}"
            )

    # --------------------------------------------------------
    # "open Amma's chat"
    # --------------------------------------------------------

    if command.startswith("open ") and command.endswith("'s chat"):

        contact = command[
            len("open "):-len("'s chat")
        ].strip()

        if contact:

            return handle_whatsapp(
                f"whatsapp search for {contact}"
            )

    # --------------------------------------------------------
    # "open chat with Amma"
    # --------------------------------------------------------

    for phrase in chat_phrases:

        if command.startswith(phrase):

            contact = command.replace(
                phrase,
                "",
                1
            ).strip()

            if contact:

                # Remove possessive ending if voice recognition adds it
                if contact.endswith("'s"):
                    contact = contact[:-2].strip()

                return handle_whatsapp(
                    f"whatsapp search for {contact}"
                )

    return None


# ============================================================
# MAIN
# ============================================================

def main():

    speak("Friday online. Ready Dev.")

    start_reminder_checker(speak)

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower().strip()

        print("🧑 You:", command)

        # ====================================================
        # EXIT
        # ====================================================

        if command in [
            "exit",
            "bye",
            "quit",
            "stop"
        ]:

            speak("Going offline")
            break

        # ====================================================
        # MEMORY
        # ====================================================

        memory_response = handle_memory(command)

        if memory_response:

            speak(memory_response)
            continue

        # ====================================================
        # WHATSAPP CHAT
        # ====================================================

        whatsapp_chat_response = handle_whatsapp_chat_open(
            command
        )

        if whatsapp_chat_response:

            speak(whatsapp_chat_response)
            continue

        # ====================================================
        # WHATSAPP
        # ====================================================

        whatsapp_response = handle_whatsapp(command)

        if whatsapp_response:

            speak(whatsapp_response)
            continue

        # ====================================================
        # NOTES
        # ====================================================

        notes_response = handle_notes(command)

        if notes_response:

            speak(notes_response)
            continue

        # ====================================================
        # REMINDER
        # ====================================================

        if command.startswith("remind me"):

            response = handle_reminder(command)

            if response:
                speak(response)

            continue

        # ====================================================
        # GREETINGS
        # ====================================================

        if (
            command == "hello"
            or command == "hi"
            or command.startswith("hello ")
            or command.startswith("hi ")
        ):

            speak("Hello Dev.")
            continue

        # ====================================================
        # GOOGLE
        # ====================================================

        if command == "open google":

            speak(open_google())
            continue

        # ====================================================
        # YOUTUBE
        # ====================================================

        if command == "open youtube":

            speak(open_youtube())
            continue

        # ====================================================
        # YOUTUBE SEARCH
        # ====================================================

        if command.startswith("search youtube for"):

            query = command.replace(
                "search youtube for",
                "",
                1
            ).strip()

            if query:

                speak(search_youtube(query))

            else:

                speak(
                    "What should I search on YouTube?"
                )

            continue

        # ====================================================
        # GOOGLE SEARCH
        # ====================================================

        if command.startswith("search for"):

            query = command.replace(
                "search for",
                "",
                1
            ).strip()

            if query:

                speak(search_google(query))

            else:

                speak("What should I search?")

            continue

        # ====================================================
        # GENERAL SEARCH
        # ====================================================

        if command.startswith("search"):

            query = command.replace(
                "search",
                "",
                1
            ).strip()

            if query:

                speak(search_google(query))

            else:

                speak("What should I search?")

            continue

        # ====================================================
        # MAC CONTROLS
        # ====================================================

        if (
            "time" in command
            or "date" in command
            or "today" in command
            or "battery" in command
            or "screenshot" in command
            or "increase volume" in command
            or "decrease volume" in command
            or "mute" in command
            or "lock" in command
            or "sleep" in command
            or command.startswith("close ")
        ):

            speak(
                execute_mac_command(command)
            )

            continue

        # ====================================================
        # OPEN APP / WEBSITE / FOLDER
        # ====================================================

        if command.startswith("open"):

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

            continue

        # ====================================================
        # AI BRAIN
        # ====================================================

        speak("Let me think.")

        response = ask_friday(command)

        speak(response)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()
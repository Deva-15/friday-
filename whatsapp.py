import subprocess
import time
import os


# ============================================================
# WHATSAPP CONFIGURATION
# ============================================================

WHATSAPP_PATH = "/Applications/\u200eWhatsApp.app"
WHATSAPP_PROCESS = "\u200eWhatsApp"


# ============================================================
# OPEN WHATSAPP
# ============================================================

def open_whatsapp():

    if not os.path.exists(WHATSAPP_PATH):
        return "I couldn't find WhatsApp."

    try:

        subprocess.run(
            ["open", WHATSAPP_PATH],
            check=True
        )

        time.sleep(2)

        return "Opening WhatsApp."

    except Exception as error:

        print("WhatsApp open error:", error)

        return "I couldn't open WhatsApp."


# ============================================================
# SEARCH WHATSAPP AND OPEN CHAT
# ============================================================

def search_whatsapp(query):

    query = query.strip()

    if not query:
        return "Who should I search for on WhatsApp?"

    if not os.path.exists(WHATSAPP_PATH):
        return "I couldn't find WhatsApp."

    try:

        # ----------------------------------------------------
        # OPEN WHATSAPP
        # ----------------------------------------------------

        subprocess.run(
            ["open", WHATSAPP_PATH],
            check=True
        )

        time.sleep(2)


        # ----------------------------------------------------
        # ESCAPE TEXT FOR APPLESCRIPT
        # ----------------------------------------------------

        escaped_query = (
            query
            .replace("\\", "\\\\")
            .replace('"', '\\"')
        )


        # ----------------------------------------------------
        # WHATSAPP UI AUTOMATION
        # ----------------------------------------------------

        script = f'''
        tell application "System Events"

            tell process "{WHATSAPP_PROCESS}"

                set frontmost to true

                delay 1


                -- =========================================
                -- OPEN WHATSAPP SEARCH
                -- =========================================

                keystroke "f" using command down

                delay 1


                -- =========================================
                -- CLEAR SEARCH FIELD
                -- =========================================

                keystroke "a" using command down

                delay 0.3


                -- =========================================
                -- TYPE CONTACT NAME
                -- =========================================

                keystroke "{escaped_query}"

                delay 2


                -- =========================================
                -- MOVE FROM SEARCH BOX TO RESULTS
                -- =========================================

                keystroke tab

                delay 0.5

                keystroke tab

                delay 0.5


                -- =========================================
                -- SELECT FIRST SEARCH RESULT
                -- =========================================

                key code 125

                delay 0.5

                key code 36

                delay 2


            end tell

        end tell
        '''


        # ----------------------------------------------------
        # RUN APPLESCRIPT
        # ----------------------------------------------------

        result = subprocess.run(
            [
                "osascript",
                "-e",
                script
            ],
            capture_output=True,
            text=True
        )


        # ----------------------------------------------------
        # CHECK FOR ERRORS
        # ----------------------------------------------------

        if result.returncode != 0:

            print(
                "WhatsApp automation error:"
            )

            print(result.stderr)

            return (
                "I searched WhatsApp, but I couldn't "
                "open the chat. Please check Accessibility "
                "permission for Terminal."
            )


        # Give WhatsApp time to open chat
        time.sleep(1)


        return f"Opened the WhatsApp chat for {query}."


    except Exception as error:

        print(
            "WhatsApp search error:",
            error
        )

        return "I couldn't search WhatsApp."


# ============================================================
# HANDLE WHATSAPP COMMANDS
# ============================================================

def handle_whatsapp(command):

    command = command.lower().strip()


    # ========================================================
    # OPEN WHATSAPP
    # ========================================================

    if command in [
        "open whatsapp",
        "open whats app",
        "start whatsapp"
    ]:

        return open_whatsapp()


    # ========================================================
    # SEARCH / OPEN CHAT
    # ========================================================

    search_phrases = [

        "send message to",

        "message",

        "open chat with",

        "open chat",

        "chat with",

        "in whatsapp search for",

        "in whatsapp search",

        "whatsapp search for",

        "whatsapp search",

        "search whatsapp for",

        "search whatsapp"
    ]


    for phrase in search_phrases:

        if command.startswith(phrase):

            query = command.replace(
                phrase,
                "",
                1
            ).strip()


            if not query:

                return (
                    "Who should I open "
                    "on WhatsApp?"
                )


            # Remove possessive "'s"
            if query.endswith("'s"):
                query = query[:-2].strip()


            return search_whatsapp(query)


    return None
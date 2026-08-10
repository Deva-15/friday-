import subprocess
from datetime import datetime


# ============================================================
# TIME
# ============================================================

def get_time():
    now = datetime.now().strftime("%I:%M %p")
    return f"The time is {now}"


# ============================================================
# DATE
# ============================================================

def get_date():
    today = datetime.now().strftime("%A, %d %B %Y")
    return f"Today is {today}"


# ============================================================
# BATTERY
# ============================================================

def get_battery():
    try:
        result = subprocess.run(
            [
                "pmset",
                "-g",
                "batt"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout

        # Find percentage
        import re

        match = re.search(
            r"(\d+)%.*?(\w+)",
            output
        )

        if match:
            percentage = match.group(1)

            return f"Battery is at {percentage} percent."

        return "I couldn't read the battery percentage."

    except Exception:
        return "Unable to check the battery."


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot():

    filename = datetime.now().strftime(
        "Screenshot-%Y%m%d-%H%M%S.png"
    )

    path = f"{__import__('os').path.expanduser('~/Desktop')}/{filename}"

    try:

        subprocess.run(
            [
                "screencapture",
                path
            ],
            check=True
        )

        return f"Screenshot saved to your Desktop as {filename}"

    except Exception:

        return "Unable to take screenshot."


# ============================================================
# VOLUME UP
# ============================================================

def volume_up():

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output volume ((output volume of (get volume settings)) + 10)"
            ]
        )

        return "Volume increased."

    except Exception:

        return "Unable to increase volume."


# ============================================================
# VOLUME DOWN
# ============================================================

def volume_down():

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output volume ((output volume of (get volume settings)) - 10)"
            ]
        )

        return "Volume decreased."

    except Exception:

        return "Unable to decrease volume."


# ============================================================
# MUTE
# ============================================================

def mute_volume():

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume with output muted"
            ]
        )

        return "Volume muted."

    except Exception:

        return "Unable to mute volume."


# ============================================================
# LOCK SCREEN
# ============================================================

def lock_screen():

    try:

        subprocess.run(
            [
                "pmset",
                "displaysleepnow"
            ]
        )

        return "Locking the screen."

    except Exception:

        return "Unable to lock the screen."


# ============================================================
# SLEEP
# ============================================================

def sleep_mac():

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                'tell application "System Events" to sleep'
            ]
        )

        return "Putting the Mac to sleep."

    except Exception:

        return "Unable to put the Mac to sleep."


# ============================================================
# OPEN FOLDER
# ============================================================

def open_folder(folder):

    folders = {

        "downloads":
            "~/Downloads",

        "desktop":
            "~/Desktop",

        "documents":
            "~/Documents",

        "pictures":
            "~/Pictures",

        "music":
            "~/Music",

        "movies":
            "~/Movies",

        "applications":
            "/Applications"
    }

    if folder not in folders:

        return "I don't know that folder."

    path = __import__("os").path.expanduser(
        folders[folder]
    )

    try:

        subprocess.run(
            [
                "open",
                path
            ]
        )

        return f"Opening {folder}."

    except Exception:

        return f"Unable to open {folder}."


# ============================================================
# EMPTY TRASH
# ============================================================

def empty_trash():

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                'tell application "Finder" to empty trash'
            ]
        )

        return "Trash emptied."

    except Exception:

        return "Unable to empty the trash."


# ============================================================
# CLOSE APP
# ============================================================

def close_app(command):

    app_name = command.replace(
        "close",
        "",
        1
    ).strip()

    if not app_name:

        return "Which app should I close?"

    # Convert common names correctly
    app_aliases = {

        "youtube": "YouTube",

        "google chrome": "Google Chrome",

        "chrome": "Google Chrome",

        "safari": "Safari",

        "whatsapp": "WhatsApp",

        "telegram": "Telegram",

        "spotify": "Spotify",

        "finder": "Finder",

        "terminal": "Terminal",

        "visual studio code": "Visual Studio Code",

        "vs code": "Visual Studio Code",

        "vscode": "Visual Studio Code"
    }

    app_name = app_aliases.get(
        app_name.lower(),
        app_name
    )

    try:

        subprocess.run(
            [
                "osascript",
                "-e",
                f'tell application "{app_name}" to quit'
            ],
            check=True
        )

        return f"Closing {app_name}."

    except Exception:

        return f"I couldn't close {app_name}."


# ============================================================
# MAIN COMMAND HANDLER
# ============================================================

def execute_mac_command(command):

    command = command.lower().strip()

    # --------------------------------------------------------
    # CLOSE APP
    # --------------------------------------------------------

    if command.startswith("close "):

        return close_app(command)

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if "time" in command:

        return get_time()

    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif "date" in command or "today" in command:

        return get_date()

    # --------------------------------------------------------
    # BATTERY
    # --------------------------------------------------------

    elif "battery" in command:

        return get_battery()

    # --------------------------------------------------------
    # SCREENSHOT
    # --------------------------------------------------------

    elif "screenshot" in command:

        return take_screenshot()

    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    elif "increase volume" in command:

        return volume_up()

    elif "decrease volume" in command:

        return volume_down()

    elif "mute volume" in command or command == "mute":

        return mute_volume()

    # --------------------------------------------------------
    # LOCK / SLEEP
    # --------------------------------------------------------

    elif "lock" in command:

        return lock_screen()

    elif "sleep" in command:

        return sleep_mac()

    # --------------------------------------------------------
    # FOLDERS
    # --------------------------------------------------------

    elif (
        "open downloads" in command
        or "open download" in command
    ):

        return open_folder("downloads")

    elif "open desktop" in command:

        return open_folder("desktop")

    elif (
        "open documents" in command
        or "open document" in command
    ):

        return open_folder("documents")

    elif (
        "open pictures" in command
        or "open picture" in command
    ):

        return open_folder("pictures")

    elif "open music" in command:

        return open_folder("music")

    elif "open movies" in command:

        return open_folder("movies")

    elif "open applications" in command:

        return open_folder("applications")

    # --------------------------------------------------------
    # TRASH
    # --------------------------------------------------------

    elif "empty trash" in command:

        return empty_trash()

    # --------------------------------------------------------
    # UNKNOWN
    # --------------------------------------------------------

    return "Command not recognized"
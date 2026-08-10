import json
import os
import threading
import time
from datetime import datetime

REMINDER_FILE = "memory/reminders.json"


def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []

    try:
        with open(REMINDER_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return []


def save_reminders(reminders):
    os.makedirs("memory", exist_ok=True)

    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(reminder_time, message):
    reminders = load_reminders()

    reminders.append({
        "time": reminder_time,
        "message": message,
        "completed": False
    })

    save_reminders(reminders)

    return f"Reminder set for {reminder_time}: {message}"


def reminder_checker(speak_function):

    while True:

        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        reminders = load_reminders()
        changed = False

        for reminder in reminders:

            if (
                reminder["time"] == now
                and not reminder["completed"]
            ):

                speak_function(
                    f"Reminder: {reminder['message']}"
                )

                reminder["completed"] = True
                changed = True

        if changed:
            save_reminders(reminders)

        time.sleep(20)


def start_reminder_checker(speak_function):

    thread = threading.Thread(
        target=reminder_checker,
        args=(speak_function,),
        daemon=True
    )

    thread.start()
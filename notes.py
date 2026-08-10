import subprocess


def create_note(title, body):
    """
    Create a new note in the macOS Notes app.
    """

    title = title.replace('"', '\\"')
    body = body.replace('"', '\\"')

    script = f'''
    tell application "Notes"
        tell account "iCloud"
            make new note with properties {{name:"{title}", body:"{body}"}}
        end tell
    end tell
    '''

    try:
        subprocess.run(
            ["osascript", "-e", script],
            check=True,
            capture_output=True,
            text=True
        )

        return f"Note created: {title}"

    except subprocess.CalledProcessError as error:
        print("Notes error:", error.stderr)
        return "I couldn't create the note."


def open_notes():
    """
    Open the macOS Notes application.
    """

    try:
        subprocess.run(
            ["open", "-a", "Notes"],
            check=True
        )

        return "Opening Notes."

    except Exception:
        return "I couldn't open Notes."


def create_quick_note(body):
    """
    Create a quick note using the first few words
    as the title.
    """

    words = body.split()

    if not words:
        return "There is nothing to write."

    title = " ".join(words[:6])

    if len(words) > 6:
        title += "..."

    return create_note(title, body)
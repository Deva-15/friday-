import subprocess
import time

PROCESS = "\u200eWhatsApp"

script = f'''
tell application "System Events"
    tell process "{PROCESS}"
        set frontmost to true
        delay 1

        keystroke "f" using command down
        delay 1

        keystroke "a" using command down
        keystroke "Amma"

        delay 3

        log "===== WINDOWS ====="

        repeat with w in windows
            log "WINDOW: " & (name of w)

            repeat with e in UI elements of w
                try
                    log "ELEMENT: " & (role description of e) & " | " & (description of e)
                end try
            end repeat
        end repeat
    end tell
end tell
'''

result = subprocess.run(
    ["osascript", "-e", script],
    capture_output=True,
    text=True
)

print("RETURN CODE:", result.returncode)
print("OUTPUT:")
print(result.stdout)
print("ERROR:")
print(result.stderr)
import os
import subprocess


def open_app(name):

    name = name.lower()

    for folder in [
        "/Applications",
        "/System/Applications"
    ]:

        if os.path.exists(folder):

            for app in os.listdir(folder):

                if name in app.lower():

                    subprocess.Popen(
                        [
                            "open",
                            os.path.join(folder, app)
                        ]
                    )

                    return f"Opening {app.replace('.app','')}"


    return "App not found"
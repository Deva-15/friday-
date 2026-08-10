import subprocess

def speak(text):
    print("🤖 Friday:", text)
    subprocess.run(["say", text])
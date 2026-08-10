import webbrowser
import urllib.parse

# Open Websites
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
    "facebook": "https://www.facebook.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "x": "https://x.com",
    "twitter": "https://x.com"
}


def open_google():
    webbrowser.open(WEBSITES["google"])
    return "Opening Google"


def open_youtube():
    webbrowser.open(WEBSITES["youtube"])
    return "Opening YouTube"


def search_google(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Searching Google for {query}"


def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Searching YouTube for {query}"


def open_website(name):
    name = name.lower().strip()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        return f"Opening {name.title()}"

    if "." in name:
        webbrowser.open("https://" + name)
        return f"Opening {name}"

    return None
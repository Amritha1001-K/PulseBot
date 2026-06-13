import requests
from datetime import datetime

# Get weather
def get_weather():
    try:
        response = requests.get("https://wttr.in/?format=3")
        return response.text
    except Exception as e:
        return f"Weather error: {e}"

# Get quote
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        return f"{data['q']} — {data['a']}"
    except Exception as e:
        return f"Quote error: {e}"

# Create summary
def create_summary():
    weather = get_weather()
    quote = get_quote()

    summary = f"""
DAILY PULSE REPORT
==================

Date: {datetime.now()}

Weather:
{weather}

Quote:
{quote}
"""

    print(summary)

    with open("daily_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print("Summary saved!")

if __name__ == "__main__":
    create_summary()
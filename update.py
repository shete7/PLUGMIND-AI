import requests
import os

SERVER_URL = "https://raw.githubusercontent.com/shete7/PlugMind-AI/main"
VERSION_FILE = "version.txt"
AI_SCRIPT = "assistant.py"

def check_update():
    try:
        latest_version = requests.get(f"{SERVER_URL}/version.txt").text.strip()
        if os.path.exists(VERSION_FILE):
            with open(VERSION_FILE, "r") as file:
                current_version = file.read().strip()
        else:
            current_version = "0"

        if latest_version != current_version:
            print("🔄 New update found! Downloading...")
            ai_code = requests.get(f"{SERVER_URL}/assistant.py").text
            with open(AI_SCRIPT, "w") as file:
                file.write(ai_code)
            with open(VERSION_FILE, "w") as file:
                file.write(latest_version)
            print("✅ Update installed successfully!")
        else:
            print("🔹 Already up to date.")
    except Exception as e:
        print(f"❌ Error checking update: {e}")

if __name__ == "__main__":
    check_update()

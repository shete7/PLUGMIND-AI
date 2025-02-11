import os
import requests
import speech_recognition as sr
import openai
import pyautogui
import pdfplumber

OPENAI_API_KEY = "your-open-source-api-key"

def is_online():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def run_ai():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🗣 Say something...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"👤 You: {text}")

        if "search file" in text:
            filename = text.replace("search file", "").strip()
            search_file(filename)
        elif "schedule" in text:
            pyautogui.alert(f"Scheduled Task: {text}")
        else:
            if is_online():
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": text}],
                    api_key=OPENAI_API_KEY
                )
                print(f"🤖 AI: {response['choices'][0]['message']['content']}")

    except sr.UnknownValueError:
        print("🤖 AI: Sorry, I didn't catch that.")

if __name__ == "__main__":
    run_ai()

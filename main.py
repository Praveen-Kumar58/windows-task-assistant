import pyttsx3
import speech_recognition as sr
import webbrowser
import os


def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"⚠️ Error with the request to Google API: {e}")
        return ""


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        text_to_speech("I am listening")
        command = convert_speech_to_text()

        if 'open instagram' in command:
            webbrowser.open("https://www.instagram.com")

        elif 'control panel' in command:
            os.system("control panel")

        elif 'youtube' in command or 'you tube' in command:
            webbrowser.open("https://www.youtube.com")

        elif 'netflix' in command:
            webbrowser.open("https://www.netflix.com")

        elif 'exit' in command or 'quit' in command:
            text_to_speech("Goodbye. See you again.")
            break

        else:
            text_to_speech("I don't understand that command.")


if __name__ == "__main__":
    main()

import os

from kivy.core.audio import SoundLoader
from kivy.utils import platform


class AudioManager:
    def __init__(self):
        self.current_sound = None

    def speak(self, text):
        """Speak a word using the device's text-to-speech engine."""
        try:
            if platform == "android":
                from plyer import tts
                tts.speak(text)
            else:
                import pyttsx3

                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
                engine.stop()
        except Exception as error:
            print("Speech error:", error)

    def play_sound(self, sound_path):
        """Play a WAV or other supported audio file."""
        if not sound_path or not os.path.isfile(sound_path):
            print("Sound file not found:", sound_path)
            return

        try:
            if self.current_sound:
                self.current_sound.stop()

            self.current_sound = SoundLoader.load(sound_path)

            if self.current_sound:
                self.current_sound.play()
            else:
                print("Unable to load sound:", sound_path)

        except Exception as error:
            print("Audio error:", error)

    def play_item(self, item):
        """Speak the name and play its sound when available."""
        self.speak(item["name"])

        sound_path = item.get("sound")
        if sound_path:
            self.play_sound(sound_path)

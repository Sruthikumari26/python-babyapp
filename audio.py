import os
from kivy.core.audio import SoundLoader
from kivy.utils import platform


class AudioManager:

    def __init__(self):
        self.current_sound = None
        self.engine = None

        # Initialize desktop speech engine once
        if platform != "android":
            try:
                import pyttsx3
                self.engine = pyttsx3.init()
                self.engine.setProperty("rate", 125)
                self.engine.setProperty("volume", 1.0)
            except Exception as error:
                print("TTS initialization error:", error)

    def speak(self, text):
        """Speak slowly and clearly for baby learning."""
        try:
            if platform == "android":
                from plyer import tts
                tts.speak(text)

            elif self.engine:
                self.engine.say(text)
                self.engine.runAndWait()

        except Exception as error:
            print("Speech error:", error)

    def play_sound(self, sound_path):
        """Play an optional individual audio recording."""
        if not sound_path or not os.path.isfile(sound_path):
            print("Sound file not found:", sound_path)
            return

        try:
            if self.current_sound:
                self.current_sound.stop()

            self.current_sound = SoundLoader.load(sound_path)

            if self.current_sound:
                self.current_sound.play()

        except Exception as error:
            print("Audio error:", error)
            
def play_item(self, item):
    """Speak a fun, baby-friendly vehicle name when tapped."""

    name = item["name"]

    pronunciations = {
        "Car": "Caaaaaaarrrrr!",
        "Bus": "Buuuuuus!",
        "Train": "Traaaaaain!",
        "Airplane": "Aaaaaairplaaaane!",
        "Ship": "Shiiiiip!",
        "Bicycle": "Biiiiicycle!",
        "Truck": "Truuuuuck!",
        "Helicopter": "Heliiiiicopter!",
    }

    message = pronunciations.get(name, name)

    self.speak(message)

            
      

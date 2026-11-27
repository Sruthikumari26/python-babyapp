"""
BABY LEARNING SCHOOL 🌈
A gentle, touch-friendly first-learning app for babies (0–12 months).

Desktop:
    python -m pip install -r requirements.txt
    python main.py

Android:
    See README.txt. Build with Buildozer on Linux/WSL.

Speech:
- Android: uses the device's installed speech service through Plyer when available.
- Desktop: uses pyttsx3 when installed.
Sound effects are generated locally (no internet required). They are playful
sound effects, not recordings of real animals or vehicles.
"""
import os
import math
import wave
import struct
import tempfile
import threading

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.utils import platform

try:
    from plyer import tts as plyer_tts
except Exception:
    plyer_tts = None

try:
    import pyttsx3
except Exception:
    pyttsx3 = None

BG = (1.00, 0.97, 0.91, 1)
INK = (0.16, 0.22, 0.27, 1)
MUTED = (0.35, 0.43, 0.48, 1)
PASTELS = [
    (1.00, 0.88, 0.72, 1), (0.79, 0.91, 0.81, 1),
    (0.76, 0.87, 0.98, 1), (0.98, 0.81, 0.86, 1),
    (0.86, 0.82, 0.95, 1), (1.00, 0.95, 0.69, 1),
]

LESSONS = {
    "Transport": {
        "icon": "🚗", "intro": "Let's explore things that go!",
        "items": [
            ("Car", "🚗", "A car. Vroom, vroom!", "car"),
            ("Bus", "🚌", "A bus. Beep, beep!", "horn"),
            ("Train", "🚂", "A train. Choo, choo!", "train"),
            ("Airplane", "✈️", "An airplane. Whoooosh!", "plane"),
            ("Boat", "⛵", "A boat. Splash, splash!", "water"),
            ("Bicycle", "🚲", "A bicycle. Ring, ring!", "bell"),
        ],
    },
    "Animals": {
        "icon": "🐾", "intro": "Hello, little animal friends!",
        "items": [
            ("Dog", "🐶", "A dog says woof, woof!", "dog"),
            ("Cat", "🐱", "A cat says meow!", "cat"),
            ("Cow", "🐮", "A cow says moo!", "cow"),
            ("Duck", "🦆", "A duck says quack, quack!", "duck"),
            ("Lion", "🦁", "A lion says roar!", "lion"),
            ("Bird", "🐦", "A bird says tweet, tweet!", "bird"),
        ],
    },
    "Numbers": {
        "icon": "🔢", "intro": "Let's look at numbers together!",
        "items": [
            ("One", "1", "One. One little star.", "number"),
            ("Two", "2", "Two. Two little dots.", "number"),
            ("Three", "3", "Three. One, two, three!", "number"),
            ("Four", "4", "Four. Four little flowers.", "number"),
            ("Five", "5", "Five. Five little fingers.", "number"),
            ("Six", "6", "Six. Let's count to six.", "number"),
            ("Seven", "7", "Seven. Seven little stars.", "number"),
            ("Eight", "8", "Eight. Eight little dots.", "number"),
            ("Nine", "9", "Nine. Nearly ten!", "number"),
            ("Ten", "10", "Ten! Well done!", "number"),
        ],
    },
}

# Tiny local sound generator: playful tones and rhythms, no downloaded files.
def make_sound(kind, folder):
    path = os.path.join(folder, kind + ".wav")
    if os.path.exists(path):
        return path
    rate, duration = 22050, 0.85
    samples = []
    for i in range(int(rate * duration)):
        t = i / rate
        env = min(1, t * 18) * min(1, (duration - t) * 12)
        if kind in ("horn", "car", "train"):
            freq = 440 if kind == "horn" else (180 + 30 * math.sin(t * 9) if kind == "car" else 310)
            val = math.sin(2 * math.pi * freq * t)
            if kind == "train":
                val *= 0.55 + 0.45 * math.sin(2 * math.pi * 3 * t)
        elif kind == "bell":
            val = math.sin(2 * math.pi * 880 * t) * math.exp(-4 * t)
            val += 0.35 * math.sin(2 * math.pi * 1320 * t) * math.exp(-5 * t)
        elif kind == "plane":
            freq = 240 + 140 * t
            val = math.sin(2 * math.pi * freq * t)
        elif kind == "water":
            val = math.sin(2 * math.pi * (500 + 250 * math.sin(t * 16)) * t) * 0.45
        elif kind == "dog":
            val = (math.sin(2 * math.pi * 170 * t) + 0.3 * math.sin(2 * math.pi * 340 * t))
            env *= 1 if t < .32 or t > .48 else .08
        elif kind == "cat":
            val = math.sin(2 * math.pi * (500 + 180 * t) * t) * (0.6 + 0.4 * math.sin(2 * math.pi * 5 * t))
        elif kind == "cow":
            val = math.sin(2 * math.pi * 115 * t) * (0.7 + 0.3 * math.sin(2 * math.pi * 4 * t))
        elif kind == "duck":
            val = math.sin(2 * math.pi * 390 * t) * (0.6 + 0.4 * math.sin(2 * math.pi * 7 * t))
        elif kind == "lion":
            val = math.sin(2 * math.pi * (95 + 18 * math.sin(t * 20)) * t)
            val *= 0.7 + 0.3 * math.sin(2 * math.pi * 18 * t)
        elif kind == "bird":
            val = math.sin(2 * math.pi * (1000 + 350 * math.sin(t * 28)) * t)
            env *= 0.65 + 0.35 * math.sin(t * 35) ** 2
        else:
            val = math.sin(2 * math.pi * 440 * t)
        samples.append(int(max(-1, min(1, val * env * 0.23)) * 32767))
    with wave.open(path, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(rate)
        f.writeframes(b"".join(struct.pack("<h", s) for s in samples))
    return path


class SoftPanel(BoxLayout):
    def __init__(self, color=(1, 1, 1, 1), radius=24, **kwargs):
        super().__init__(**kwargs)
        self.panel_color = color
        self.radius = radius
        with self.canvas.before:
            Color(*color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(radius)])
        self.bind(pos=self._sync, size=self._sync)

    def _sync(self, *_):
        self.rect.pos = self.pos
        self.rect.size = self.size


class BabyButton(Button):
    def __init__(self, bg=(1, 1, 1, 1), font_size="20sp", **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = bg
        self.color = INK
        self.font_size = font_size
        self.bold = True
        self.halign = "center"
        self.valign = "middle"
        self.bind(size=lambda inst, val: setattr(inst, "text_size", (val[0]-dp(12), val[1]-dp(8))))


class BabyLearningApp(App):
    def build(self):
        self.title = "Baby Learning School"
        self.sound_dir = os.path.join(tempfile.gettempdir(), "baby_learning_sounds")
        os.makedirs(self.sound_dir, exist_ok=True)
        self.current_category = None
        self.current_index = 0
        self.current_sound = None
        self.tts_engine = None
        self.tts_lock = threading.Lock()
        self._init_speech()
        Window.clearcolor = BG
        self.root_box = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(10))
        self.show_home()
        return self.root_box

    def _init_speech(self):
        if platform == "android":
            return
        if pyttsx3:
            try:
                self.tts_engine = pyttsx3.init()
                self.tts_engine.setProperty("rate", 135)
                self.tts_engine.setProperty("volume", 0.85)
            except Exception:
                self.tts_engine = None

    def speak(self, words):
        if platform == "android" and plyer_tts:
            try:
                plyer_tts.speak(words)
                return
            except Exception:
                pass
        if self.tts_engine:
            def run():
                with self.tts_lock:
                    try:
                        self.tts_engine.stop()
                        self.tts_engine.say(words)
                        self.tts_engine.runAndWait()
                    except Exception:
                        pass
            threading.Thread(target=run, daemon=True).start()

    def play_effect(self, kind):
        try:
            if self.current_sound:
                self.current_sound.stop()
            path = make_sound(kind, self.sound_dir)
            self.current_sound = SoundLoader.load(path)
            if self.current_sound:
                self.current_sound.volume = 0.35
                self.current_sound.play()
        except Exception:
            pass

    def reset(self):
        self.root_box.clear_widgets()

    def heading(self, title, subtitle):
        title_label = Label(text=title, color=INK, font_size="29sp",
                            bold=True, size_hint_y=None, height=dp(48))
        sub = Label(text=subtitle, color=MUTED, font_size="15sp",
                    size_hint_y=None, height=dp(32))
        self.root_box.add_widget(title_label)
        self.root_box.add_widget(sub)

    def show_home(self, *_):
        self.reset()
        self.current_category = None
        self.heading("🌈 Baby Learning School", "Little eyes, little ears, big discoveries!")
        welcome = SoftPanel(orientation="vertical", size_hint_y=None, height=dp(112),
                            padding=dp(12), color=(1, .91, .76, 1))
        welcome.add_widget(Label(text="Hello, little sunshine! ☀️", color=INK,
                                 bold=True, font_size="23sp"))
        welcome.add_widget(Label(text="Tap a picture with your grown-up.",
                                 color=MUTED, font_size="16sp"))
        self.root_box.add_widget(welcome)

        for title, emoji, desc, color in [
            ("Animals", "🐶", "Meet friendly animal friends", PASTELS[1]),
            ("Transport", "🚗", "Explore things that go", PASTELS[0]),
            ("Numbers", "🔢", "See numbers from one to ten", PASTELS[2]),
        ]:
            card = SoftPanel(orientation="horizontal", size_hint_y=None, height=dp(112),
                             padding=dp(8), spacing=dp(10), color=color)
            icon = Label(text=emoji, font_size="45sp", size_hint_x=.30)
            words = BoxLayout(orientation="vertical")
            words.add_widget(Label(text=title, color=INK, font_size="23sp", bold=True,
                                   halign="left"))
            words.add_widget(Label(text=desc, color=MUTED, font_size="14sp",
                                   halign="left"))
            card.add_widget(icon)
            card.add_widget(words)
            btn = BabyButton(text="LET'S GO  ➜", bg=color, size_hint_x=.38, font_size="17sp")
            btn.bind(on_release=lambda _b, c=title: self.open_category(c))
            card.add_widget(btn)
            self.root_box.add_widget(card)

        self.root_box.add_widget(Widget())
        footer = Label(text="A calm little learning moment • Learn together ❤️",
                       color=MUTED, font_size="12sp", size_hint_y=None, height=dp(28))
        self.root_box.add_widget(footer)

    def open_category(self, category):
        self.current_category = category
        self.current_index = 0
        self.show_card()

    def show_card(self, *_):
        self.reset()
        data = LESSONS[self.current_category]
        items = data["items"]
        name, picture, phrase, sound = items[self.current_index]
        self.heading(data["icon"] + "  " + self.current_category,
                     data["intro"])

        counter = Label(text=f"{self.current_index + 1} of {len(items)}",
                        color=MUTED, font_size="13sp", size_hint_y=None, height=dp(22))
        self.root_box.add_widget(counter)

        color = PASTELS[self.current_index % len(PASTELS)]
        card = SoftPanel(orientation="vertical", padding=dp(12), spacing=dp(5),
                         color=color)
        card.add_widget(Widget(size_hint_y=.08))
        art = Label(text=picture, font_size="100sp", color=INK)
        card.add_widget(art)
        name_label = Label(text=name, font_size="34sp", bold=True, color=INK,
                           size_hint_y=None, height=dp(52))
        card.add_widget(name_label)
        if self.current_category == "Numbers":
            dots = "   ".join(["●"] * int(picture))
            card.add_widget(Label(text=dots, color=(.20, .48, .70, 1),
                                  font_size="22sp", size_hint_y=None, height=dp(48)))
        card.add_widget(Label(text=phrase, color=MUTED, font_size="19sp",
                              size_hint_y=None, height=dp(44)))
        card.add_widget(Widget(size_hint_y=.08))
        self.root_box.add_widget(card)

        controls = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(124))
        voice = BabyButton(text="🔊  HEAR WORD", bg=(1, .75, .38, 1), font_size="18sp")
        voice.bind(on_release=lambda *_: self.speak(f"{name}. {phrase}"))
        effect = BabyButton(text="🎵  SOUND", bg=(.68, .86, .72, 1), font_size="18sp")
        effect.bind(on_release=lambda *_: self.play_effect(sound))
        controls.add_widget(voice)
        controls.add_widget(effect)
        back = BabyButton(text="⬅  PREVIOUS", bg=(.84, .86, .89, 1), font_size="16sp")
        back.bind(on_release=self.previous)
        nxt = BabyButton(text="NEXT  ➜", bg=(.65, .82, .98, 1), font_size="16sp")
        nxt.bind(on_release=self.next)
        controls.add_widget(back)
        controls.add_widget(nxt)
        self.root_box.add_widget(controls)

        home = BabyButton(text="⌂  HOME", bg=(1, .96, .88, 1), font_size="15sp",
                          size_hint_y=None, height=dp(42))
        home.bind(on_release=self.show_home)
        self.root_box.add_widget(home)

        # Speak the word only after an intentional tap; no surprise autoplay.
        (Animation(font_size=dp(108), duration=.35) + Animation(font_size=dp(100), duration=.35)).start(art)

    def previous(self, *_):
        self.current_index = (self.current_index - 1) % len(LESSONS[self.current_category]["items"])
        self.show_card()

    def next(self, *_):
        self.current_index = (self.current_index + 1) % len(LESSONS[self.current_category]["items"])
        self.show_card()


if __name__ == "__main__":
    BabyLearningApp().run()

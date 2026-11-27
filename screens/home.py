
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=20,
            spacing=20,
            **kwargs
        )

        self.add_widget(
            Label(
                text="🌈 BABY LEARNING SCHOOL 🌈",
                font_size="28sp",
                bold=True,
                color=(0.2, 0.3, 0.7, 1),
            )
        )

        self.add_widget(
            Label(
                text="Let's Learn and Play!",
                font_size="23sp",
                color=(0.8, 0.3, 0.5, 1),
            )
        )

        self.add_menu_button("🦁 ANIMALS", "animals")
        self.add_menu_button("🚗 TRANSPORT", "transport")
        self.add_menu_button("🔢 NUMBERS", "numbers")

    def add_menu_button(self, text, screen_name):
        button = Button(
            text=text,
            font_size="25sp",
            bold=True,
            background_normal="",
            background_color=(0.95, 0.75, 0.9, 1),
        )

        button.bind(
            on_release=lambda instance: self.open_screen(screen_name)
        )

        self.add_widget(button)

    def open_screen(self, screen_name):
        self.manager.current = screen_name

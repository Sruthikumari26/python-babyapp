
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from audio import AudioManager
from ui_components import (
    create_title,
    create_grid,
    create_item_button,
    create_back_button,
)


class LessonScreen(BoxLayout):
    def __init__(self, title, items, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=10,
            **kwargs
        )

        self.audio = AudioManager()

        self.add_widget(create_title(title))

        scroll = ScrollView()
        self.grid = create_grid(columns=2)

        for item in items:
            self.grid.add_widget(
                create_item_button(item, self.on_item_pressed)
            )

        scroll.add_widget(self.grid)
        self.add_widget(scroll)

        self.add_widget(
            create_back_button(self.go_home)
        )

    def on_item_pressed(self, item):
        self.audio.play_item(item)

    def go_home(self, instance):
        self.manager.current = "home"


import os

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp


def create_title(text):
    return Label(
        text=text,
        font_size="30sp",
        bold=True,
        color=(0.2, 0.2, 0.6, 1),
        size_hint_y=None,
        height=dp(65),
    )


def create_item_button(item, callback):
    button = Button(
        text="",
        size_hint=(1, None),
        height=dp(180),
        background_normal="",
        background_color=(0.95, 0.85, 0.98, 1),
    )

    # Vertical layout for picture and name
    content = BoxLayout(
        orientation="vertical",
        padding=dp(6),
        spacing=dp(4),
    )

    image_path = item.get("image", "")

    if image_path and os.path.isfile(image_path):
        picture = Image(
            source=image_path,
            fit_mode="contain",
        )
        content.add_widget(picture)
    else:
        picture = Label(
            text=item.get("emoji", "⭐"),
            font_size="55sp",
        )
        content.add_widget(picture)

    name_label = Label(
        text=item["name"],
        font_size="20sp",
        bold=True,
        color=(0.15, 0.15, 0.2, 1),
        size_hint_y=None,
        height=dp(35),
    )

    content.add_widget(name_label)
    button.add_widget(content)

    button.bind(on_release=lambda instance: callback(item))

    return button


def create_grid(columns=2):
    grid = GridLayout(
        cols=columns,
        spacing=dp(12),
        padding=dp(12),
        size_hint_y=None,
    )

    grid.bind(minimum_height=grid.setter("height"))

    return grid


def create_back_button(callback):
    button = Button(
        text="⬅ HOME",
        font_size="20sp",
        size_hint_y=None,
        height=dp(55),
        background_normal="",
        background_color=(0.4, 0.8, 0.9, 1),
    )

    button.bind(on_release=callback)

    return button

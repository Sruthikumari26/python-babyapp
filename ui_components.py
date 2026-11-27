
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
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
        text=f"{item['emoji']}\n{item['name']}",
        font_size="25sp",
        bold=True,
        size_hint=(1, None),
        height=dp(145),
        background_normal="",
        background_color=(0.95, 0.75, 0.95, 1),
        color=(0.15, 0.15, 0.2, 1),
    )

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

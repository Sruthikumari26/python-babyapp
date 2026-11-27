from screens.common import LessonScreen
from lessons import NUMBERS


class NumbersScreen(LessonScreen):
    def __init__(self, **kwargs):
        super().__init__("🔢 LEARN NUMBERS", NUMBERS, **kwargs)

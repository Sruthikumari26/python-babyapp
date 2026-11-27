
from screens.common import LessonScreen
from lessons import ANIMALS


class AnimalsScreen(LessonScreen):
    def __init__(self, **kwargs):
        super().__init__("🦁 LEARN ANIMALS", ANIMALS, **kwargs)

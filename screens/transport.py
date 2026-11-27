from screens.common import LessonScreen
from lessons import TRANSPORT


class TransportScreen(LessonScreen):
    def __init__(self, **kwargs):
        super().__init__("🚗 LEARN TRANSPORT", TRANSPORT, **kwargs)

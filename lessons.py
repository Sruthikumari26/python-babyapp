
ANIMALS = [
    {"name": "Lion", "emoji": "🦁", "sound": "assets/sounds/animals/lion.wav"},
    {"name": "Elephant", "emoji": "🐘", "sound": "assets/sounds/animals/elephant.wav"},
    {"name": "Dog", "emoji": "🐶", "sound": "assets/sounds/animals/dog.wav"},
    {"name": "Cat", "emoji": "🐱", "sound": "assets/sounds/animals/cat.wav"},
    {"name": "Cow", "emoji": "🐮", "sound": "assets/sounds/animals/cow.wav"},
    {"name": "Monkey", "emoji": "🐵", "sound": "assets/sounds/animals/monkey.wav"},
    {"name": "Bird", "emoji": "🐦", "sound": "assets/sounds/animals/bird.wav"},
    {"name": "Duck", "emoji": "🦆", "sound": "assets/sounds/animals/duck.wav"},
]

TRANSPORT = [
    {"name": "Car", "emoji": "🚗"},
    {"name": "Bus", "emoji": "🚌"},
    {"name": "Train", "emoji": "🚂"},
    {"name": "Airplane", "emoji": "✈️"},
    {"name": "Ship", "emoji": "🚢"},
    {"name": "Bicycle", "emoji": "🚲"},
    {"name": "Truck", "emoji": "🚚"},
    {"name": "Helicopter", "emoji": "🚁"},
]

NUMBERS = [
    {"name": str(number), "emoji": str(number)}
    for number in range(1, 11)
]


def get_lesson(category):
    lessons = {
        "animals": ANIMALS,
        "transport": TRANSPORT,
        "numbers": NUMBERS,
    }
    return lessons.get(category.lower(), [])

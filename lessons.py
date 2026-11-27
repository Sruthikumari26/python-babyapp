
ANIMALS = [
    {"name": "Lion", "emoji": "🦁", "sound": "assets/sounds/animals/lion.mp3"},
    {"name": "Elephant", "emoji": "🐘", "sound": "assets/sounds/animals/elephant.mp3"},
    {"name": "Dog", "emoji": "🐶", "sound": "assets/sounds/animals/dog.mp3"},
    {"name": "Cat", "emoji": "🐱", "sound": "assets/sounds/animals/cat.mp3"},
    {"name": "giraffe", "emoji": "🐮", "sound": "assets/sounds/animals/giraffe.mp3"},
    {"name": "Monkey", "emoji": "🐵", "sound": "assets/sounds/animals/monkey.mp3"},
    {"name": "Bird", "emoji": "🐦", "sound": "assets/sounds/animals/bird.wav"},
    {"name": "Rabbit", "emoji": "🦆", "sound": "assets/sounds/animals/rabbit.mp3"},
]

TRANSPORT = [
    {
        "name": "Car",
        "emoji": "🚗",
        "sound": "assets/sounds/transport/car.wav"
    },
    {
        "name": "Bus",
        "emoji": "🚌",
        "sound": "assets/sounds/transport/bus.wav"
    },
    {
        "name": "Train",
        "emoji": "🚂",
        "sound": "assets/sounds/transport/train.wav"
    },
    {
        "name": "Airplane",
        "emoji": "✈️",
        "sound": "assets/sounds/transport/airplane.wav"
    },
    {
        "name": "Ship",
        "emoji": "🚢",
        "sound": "assets/sounds/transport/ship.wav"
    },
    {
        "name": "Bicycle",
        "emoji": "🚲",
        "sound": "assets/sounds/transport/bicycle.wav"
    },
    {
        "name": "Truck",
        "emoji": "🚚",
        "sound": "assets/sounds/transport/truck.wav"
    },
    {
        "name": "Helicopter",
        "emoji": "🚁",
        "sound": "assets/sounds/transport/helicopter.wav"
    },
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


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
        "image": "assets/transports/car.png"
    },
    {
        "name": "Bus",
        "emoji": "🚌",
        "image": "assets/transports/bus.png"
    },
    {
        "name": "Train",
        "emoji": "🚂",
        "image": "assets/transports/train.png"
    },
    {
        "name": "Airplane",
        "emoji": "✈️",
        "image": "assets/transports/airplane.png"
    },
    {
        "name": "Ship",
        "emoji": "🚢",
        "image": "assets/transports/ship.png"
    },
    {
        "name": "Bicycle",
        "emoji": "🚲",
        "image": "assets/transports/bicycle.png"
    },
    {
        "name": "Truck",
        "emoji": "🚚",
        "image": "assets/transports/truck.png"
    },
    {
        "name": "Helicopter",
        "emoji": "🚁",
        "image": "assets/transports/helicopter.png"
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

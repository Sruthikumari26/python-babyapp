from flask import Flask, render_template

app = Flask(__name__)

ANIMALS = [
    {"name": "Lion", "image": "images/animals/lion.png",
     "sound": "sounds/lion.mp3.wav"},
    {"name": "Elephant", "image": "images/animals/elephant.png",
     "sound": "sounds/elephant.mp3"},
    {"name": "Dog", "image": "images/animals/dog.png",
     "sound": "sounds/dog.mp3"},
    {"name": "Cat", "image": "images/animals/cat.png",
     "sound": "sounds/cat.mp3"},
    {"name": "Giraffe", "image": "images/animals/giraffe.png",
     "sound": "sounds/giraffe.mp3"},
    {"name": "Monkey", "image": "images/animals/monkey.png",
     "sound": "sounds/monkey.mp3"},
    {"name": "Bird", "image": "images/animals/bird.png",
     "sound": "sounds/bird.wav"},
    {"name": "Rabbit", "image": "images/animals/rabbit.png",
     "sound": "sounds/rabbit.mp3"},
]

VEHICLES = [
    {"name": "Car", "image": "car.png"},
    {"name": "Bus", "image": "bus.png"},
    {"name": "Train", "image": "train.png"},
    {"name": "Airplane", "image": "airplane.png"},
    {"name": "Ship", "image": "ship.png"},
    {"name": "Bicycle", "image": "bicycle.png"},
    {"name": "Truck", "image": "truck.png"},
    {"name": "Helicopter", "image": "helicopter.png"},
]

NUMBERS = list(range(1, 11))


@app.route("/")
def home():
    return render_template(
        "index.html",
        animals=ANIMALS,
        vehicles=VEHICLES,
        numbers=NUMBERS
    )


@app.route("/assets/<path:filename>")
def assets(filename):
    from flask import send_from_directory
    return send_from_directory("assets", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
PY

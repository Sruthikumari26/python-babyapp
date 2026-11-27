
# 🌈 Baby Learning School

A colorful Python learning application for babies and toddlers, built using Kivy.

## Features

- Learn animal names.
- Learn transport names.
- Learn numbers from 1 to 10.
- Large, colorful touch-friendly buttons.
- Text-to-speech for learning words.
- Optional animal sound effects.
- Desktop and Android project support.
- Docker and Jenkins CI pipeline.

## Project Structure

```text
baby_learning_school/
├── main.py
├── lessons.py
├── audio.py
├── ui_components.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── compose.yml
├── buildozer.spec
├── .dockerignore
├── README.md
├── screens/
│   ├── __init__.py
│   ├── common.py
│   ├── home.py
│   ├── animals.py
│   ├── transport.py
│   └── numbers.py
├── assets/
│   ├── images/
│   │   ├── animals/
│   │   ├── transport/
│   │   └── numbers/
│   └── sounds/
│       ├── animals/
│       ├── transport/
│       └── numbers/
└── tests/
    └── test_lessons.py
```

## Install Python packages

```bash
python -m pip install -r requirements.txt
```

## Run the application

```bash
python main.py
```

## Add animal sounds

Place WAV files in:

```text
assets/sounds/animals/
```

Use these filenames:

- lion.wav
- elephant.wav
- dog.wav
- cat.wav
- cow.wav
- monkey.wav
- bird.wav
- duck.wav

The filenames must match the paths in `lessons.py`.

## Run unit tests

```bash
python -m unittest discover -s tests -v
```

## Build Docker image

```bash
docker build -t sruthikumari94/baby-learning-school:latest .
```

## Run tests using Docker Compose

```bash
docker compose up --build
```

## Android APK

Install Buildozer in a supported Linux environment and run:

```bash
buildozer android debug
```

The generated APK will be placed in the `bin/` directory.

## Jenkins

Configure a Jenkins Pipeline job using:

- Repository: Sruthikumari26
- Branch: `*/main`
- Script path: `Jenkinsfile`
- Agent label: `prod`
- Docker Hub credential ID:sruthikumari94

The Jenkins agent needs Python 3 and Docker access.

## Note

The Docker image is intended for building and testing the application.
To display the Kivy graphical interface, run the app on a desktop with a
working graphical display or package it for Android.

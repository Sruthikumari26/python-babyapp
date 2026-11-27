# 🐣 Baby Learning School

A colorful, interactive, and child-friendly Python web application designed to help babies and young children learn animals, vehicles, and numbers through pictures, sounds, and speech.

## 🌟 Features

### 🦁 1. Learn Animals
- Eight colorful animal pictures.
- Individual animal audio files.
- Click an animal picture to hear its sound.
- Animals included:
  - Lion
  - Elephant
  - Dog
  - Cat
  - Giraffe
  - Monkey
  - Bird
  - Rabbit

### 🚗 2. Learn Vehicles
- Eight individual vehicle pictures.
- Click a vehicle to hear its name.
- Uses browser Text-to-Speech.
- Vehicles included:
  - Car
  - Bus
  - Train
  - Airplane
  - Ship
  - Bicycle
  - Truck
  - Helicopter

### 🔢 3. Learn Numbers
- Numbers from 1 to 10.
- Large, colorful number displays.
- Click a number to hear its pronunciation.
- Uses browser Text-to-Speech.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Web Speech API
- Docker
- Docker Compose

## 📁 Project Structure

```text
python-babyapp/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yml
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── assets/
    ├── images/
    │   └── animals/
    │       ├── lion.png
    │       ├── elephant.png
    │       ├── dog.png
    │       ├── cat.png
    │       ├── giraffe.png
    │       ├── monkey.png
    │       ├── bird.png
    │       └── rabbit.png
    │
    ├── transports/
    │   ├── car.png
    │   ├── bus.png
    │   ├── train.png
    │   ├── airplane.png
    │   ├── ship.png
    │   ├── bicycle.png
    │   ├── truck.png
    │   └── helicopter.png
    │
    └── sounds/
        ├── lion.mp3.wav
        ├── elephant.mp3
        ├── dog.mp3
        ├── cat.mp3
        ├── giraffe.mp3
        ├── monkey.mp3
        ├── bird.wav
        └── rabbit.mp3
```

## 💻 Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-babyapp.git
cd python-babyapp
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start the application

```bash
python app.py
```

### Step 4: Open in browser

```text
http://localhost:5000
```

## 🐳 Run Using Docker

### Step 1: Build Docker image

```bash
docker build -t babylearningapp:latest .
```

### Step 2: Run Docker container

```bash
docker run -d \
  --name babyapp-test \
  -p 1113:5000 \
  babylearningapp:latest
```

### Step 3: Verify container

```bash
docker ps
```

### Step 4: View application logs

```bash
docker logs babyapp-test
```

### Step 5: Access the application

Open your browser:

```text
http://YOUR_SERVER_PUBLIC_IP:1113
```

Make sure inbound TCP port 1113 is allowed in your server firewall or cloud security group.

## 📦 Docker Hub

Docker image:

```text
sruthikumari94/babylearningapp:latest
```

Push the image to Docker Hub:

```bash
docker login
docker push sruthikumari94/babylearningapp:latest
```

Pull the image:

```bash
docker pull sruthikumari94/babylearningapp:latest
```

## 🎵 Audio Functionality

-

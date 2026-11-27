cat > static/script.js <<'JS'
function speak(message) {
    if (!("speechSynthesis" in window)) {
        alert("Your browser does not support speech playback.");
        return;
    }

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(message);
    speech.lang = "en-US";
    speech.rate = 0.75;
    speech.pitch = 1.2;

    window.speechSynthesis.speak(speech);
}

function playAnimal(name, soundFile) {
    const audio = document.getElementById("animalAudio");

    audio.pause();
    audio.currentTime = 0;
    audio.src = "/assets/" + soundFile;

    audio.play().catch(() => {
        speak(name);
    });
}

function speakNumber(number) {
    const words = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten"
    ];

    speak(words[number]);
}
JS

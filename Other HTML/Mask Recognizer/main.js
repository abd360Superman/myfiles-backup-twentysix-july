var synth = window.speechSynthesis;
var utter_this = new SpeechSynthesisUtterance('Danger! No Mask!');
console.log("ml5 version: ", ml5.version);

let video;
let classifier;


function setup() {
    canvas = createCanvas(450, 300);
    canvas.center();
    video = createCapture(VIDEO);
    video.size(450, 300);
    video.hide()

    classifier = ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/z1bAq0zGI/model.json', video, modelLoaded);

    document.querySelector("#result").innerHTML = "Loading...";
}

function modelLoaded() {
    console.log("Model Loaded");
    classifyVideo();
}

function classifyVideo() {
    classifier.classify(gotResults);
}

function gotResults(error, results) {
    if (results[0].label = 'Without Mask') {
        synth.speak(utter_this);
    }
    console.log(results);
    document.querySelector("#result").innerHTML = results[0].label;
    setTimeout(classifyVideo(), 2000);
}

function draw() {
    image(video, 0, 0, 450, 300);
}
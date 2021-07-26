function start() {
    var synth = window.speechSynthesis;

    speak_data = document.getElementById("textbox").value;

    var utter_this = new SpeechSynthesisUtterance(speak_data);

    synth.speak(utter_this);
}
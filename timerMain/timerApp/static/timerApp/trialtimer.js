// Convert input interval from seconds to miliseconds
let inputInterval = 10 * 1000;
let inputIntervalBackup = inputInterval;
// Mutuable variable to store the countdown timer
let countDownTimer;

// Variable to check if the countdown is paused and save current input interval to be used when the countdown is resumed
let isPaused = false;
let pausedInputInterval;

// By reading the Utteresance API documentation I found it plays an average of 150 words per minute, test based on that
// Set the message 
let message = "Welcome to Timer Look Away! This is a trial timer, sign up now so you can make the most of your time! Say good bye to eye strain! Thanks to Timer Look Away!"
// Calculate the number of words in the message
let numWords = message.split(" ").length;
// Make an estimation of the duration of the speech in miliseconds
let messageDuration = (numWords / 150) * 60 * 1000;

// Function to start or restart the countdown
function startCountdown() {

    // Clear any existing interval
    if (countDownTimer) {
        clearInterval(countDownTimer);
    }

    // Reset the isPaused variable
    isPaused = false;

    // Update the count down every 1 second
    countDownTimer = setInterval(function () {

        // Calculate time for hours, minutes and seconds and convert to miliseconds
        let hours = Math.floor(inputInterval / (1000 * 60 * 60));
        let minutes = Math.floor((inputInterval % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((inputInterval % (1000 * 60)) / 1000);

        // Decrease the input interval every 1 second
        inputInterval -= 1000;

        // Display the result in the element with id="countdown" as an example
        document.getElementById("countdown").innerHTML = minutes + "m " + seconds + "s ";

        // If the count down is finished, play the TTs message and restart the countdown
        if (inputInterval < 0) {

            // Stop the countdown timer so the message can be played
            clearInterval(countDownTimer);

            // Play the TTs message
            playMessage(message);

            // Display the message while the message is being played instead of the countdown
            document.getElementById("countdown").innerHTML = message;

            // Show and hide the message during the estimated duration
            setTimeout(() => {
                // Restart the countdown after the message has been hidden
                inputInterval = 10 * 1000;
                startCountdown();
            }, messageDuration);
        }
    }, 1000);
}

// Fuction to play the TTs message
function playMessage(message) {
    let utterance = new SpeechSynthesisUtterance(message);
    speechSynthesis.speak(utterance);

    document.getElementById("countdown").innerHTML = message;
}

// Function to stop the countdown
function stopCountdown() {
    clearInterval(countDownTimer);
    // Reset the input interval
    inputInterval = inputIntervalBackup;

}

// Function to pause the countdown
function pauseCountdown() {
    if (!isPaused) {
        clearInterval(countDownTimer);
        isPaused = true;
        // Save current input interval to be used when the countdown is resumed
        pausedInputInterval = inputInterval;
    }
}

// Function to resume the countdown
function resumeCountdown() {
    // isPaused will be set to false in the startCountdown function
    if (isPaused) {
        // Restore the input interval to the paused value
        inputInterval = pausedInputInterval;

        // Restart the countdown
        startCountdown();
    }
}

// Set event listeners for start and stop buttons # Done!
document.getElementById("startButton").addEventListener("click", startCountdown);
document.getElementById("stopButton").addEventListener("click", stopCountdown);
document.getElementById("pauseButton").addEventListener("click", pauseCountdown);
document.getElementById("resumeButton").addEventListener("click", resumeCountdown);
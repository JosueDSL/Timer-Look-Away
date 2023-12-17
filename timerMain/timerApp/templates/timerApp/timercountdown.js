// Reference link: https://www.w3schools.com/howto/howto_js_countdown.asp
// From where I got some inspiration, the code exposed there serves a different purpose, but it helped me to better structure the idea

// Fist I'll need to display the countdown to an element on the page
// <p id="countdown"></p>

// Get input interval from the Timer model in minutes
const inputIntervalInMinutes = 100; // 100 minutes (1 hour and 40 minutes) // This input will come from the Timer model

// Check if input interval reaches the hour mark to know if is necessary to display the hours
let isHour = false;
if (inputIntervalInMinutes > 60) {
    isHour = true;
}

// Convert input interval from minutes to miliseconds
let inputInterval = inputIntervalInMinutes * 60 * 1000;

// Mutuable variable to store the countdown timer
let countDownTimer;

// Variable to check if the countdown is paused and save current input interval to be used when the countdown is resumed
let isPaused = false;
let pausedInputInterval;

// Function to start or restart the countdown
function startCountdown() {
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
        if (isHour) {
            document.getElementById("countdown").innerHTML = hours + "h " + minutes + "m " + seconds + "s ";
        } else {
            document.getElementById("countdown").innerHTML = minutes + "m " + seconds + "s ";
        }

        // If the count down is finished, play the TTs message and restart the countdown
        if (inputInterval < 0) {
            // Stop the countdown timer so the message can be played
            clearInterval(countDownTimer);
            // Display the message while the message is being played instead of the countdown
            // document.getElementById("countdown").innerHTML = `Message from Timer model {object.timers.message}`;";
            // Play the TTs message
            // TODO
            
            // Restart the countdow
            inputInterval = inputIntervalInMinutes * 60 * 1000;
            startCountdown();
        }
    }, 1000);
}

// Function to stop the countdown
function stopCountdown() {
    clearInterval(countDownTimer);
    // Reset the input interval
    inputInterval = inputIntervalInMinutes * 60 * 1000;

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

// Set event listeners for start and stop buttons
document.getElementById("startButton").addEventListener("click", startCountdown);
document.getElementById("stopButton").addEventListener("click", stopCountdown);
document.getElementById("pauseButton").addEventListener("click", pauseCountdown);
document.getElementById("resumeButton").addEventListener("click", resumeCountdown);

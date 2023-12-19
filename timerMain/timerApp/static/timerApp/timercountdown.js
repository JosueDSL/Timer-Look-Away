// Referenced link: https://www.w3schools.com/howto/howto_js_countdown.asp
// From where I got some inspiration, the code exposed there serves a different purpose, but it helped me to better structure the idea
// Referenced: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API




// Fist I'll need to display the countdown to an element on the page
// <p id="countdown"></p>

fetch('/timerApp/get_timersjson/')
.then(response => response.json())
.then(timers => {
    console.log(timers);
    timers.forEach(timer => {
        // Get input interval from the Timer model in minutes
        const inputIntervalInMinutes = timer.fields.interval;
        console.log(inputIntervalInMinutes);
        // Check if input interval reaches the hour mark to know if is necessary to display the hours
        let isHour = false;
        if (inputIntervalInMinutes > 60) {
            isHour = true;
        }

        // Convert input interval from minutes to miliseconds
        let inputInterval = inputIntervalInMinutes * 60 * 1000;
        console.log(inputInterval);
        // Mutuable variable to store the countdown timer
        let countDownTimer;

        // Variable to check if the countdown is paused and save current input interval to be used when the countdown is resumed
        let isPaused = false;
        let pausedInputInterval;

        // By reading the Utteresance API documentation I found it plays an average of 150 words per minute, test based on that
        // Get the message from the Timer model
        let message = timer.fields.message;
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
                if (isHour) {
                    document.getElementById("countdown" + timer.pk).innerHTML = hours + "h " + minutes + "m " + seconds + "s ";
                } else {
                    document.getElementById("countdown" + timer.pk).innerHTML = minutes + "m " + seconds + "s ";
                }

                // If the count down is finished, play the TTs message and restart the countdown
                if (inputInterval < 0) {

                    // Stop the countdown timer so the message can be played
                    clearInterval(countDownTimer);

                    // Play the TTs message
                    playMessage(timer.pk, timer.fields.message);

                    // Display the message while the message is being played instead of the countdown
                    document.getElementById("countdown" + timer.pk).innerHTML = timer.fields.message
                    
                    // Show and hide the message during the estimated duration
                    setTimeout(() => {
                        // Restart the countdown after the message has been hidden
                        inputInterval = inputIntervalInMinutes * 60 * 1000;
                        startCountdown();
                    }, messageDuration);
                }
            }, 1000);
        }

        // Fuction to play the TTs message
        function playMessage(timerId, message) {
            let utterance = new SpeechSynthesisUtterance(message);
            speechSynthesis.speak(utterance);

            document.getElementById("countdown" + timerId).innerHTML = message;
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

        // Set event listeners for start and stop buttons # Done!
        document.getElementById("startButton" + timer.pk).addEventListener("click", startCountdown);
        document.getElementById("stopButton" + timer.pk).addEventListener("click", stopCountdown);
        document.getElementById("pauseButton" + timer.pk).addEventListener("click", pauseCountdown);
        document.getElementById("resumeButton" + timer.pk).addEventListener("click", resumeCountdown);
    });
});
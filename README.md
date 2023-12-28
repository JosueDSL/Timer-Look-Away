# TIMER LOOK AWAY
#### Video Demo: https://youtu.be/lhpiKcd0bYw

#### Description:
Its purpose:
The idea came from a health issue I’ve gone through my entire life:  Eye pain, aching, and fatigue due intensive exposure to screens and monitors. I believe most of us have experienced it, at least once before, due several reasons like playing video games or coding for too long without looking away from the screen. The solution to this problem came from a visit to the ophthalmologist which explained to me how our eyes work, as he explained: "Our eyes have tiny muscles that help us focus, and they get tired after staring at a screen for a while, because a screen is a flat surface . Looking away every 20 minutes allows these muscles relax, reducing eye strain and fatigue.

The main goal  of “Timer Look Away” is helping everyone to prevent and solve eye fatigue by allowing the users to set as many timers as they wish, so they remember to look away, or even boost their efficiency by setting up reminders to take a break. It's a web-based application using JavaScript, Python, SQL and Django as it's framework. Allowing the users to set these reminders through the usage of 'HTML Range input' fields so the user can control how often the timer will repeat. As an extra layer of customization and effectiveness will be reminding the user to look a way through the usage of text-to-speech allowing the user to make the timer to play any sort of reminder message they want. They will be able to record and save their greetings and settings so they don't need to start from scratch every day since its main purpose is to be a life-companion that will assist you to remind you every day to look away.

Starting from this concept, the idea of just helping to reduce eye strain looked quite small compared to the actual scope this project could have, so it ended up taking some taste-like productivity and time managment concept. Keeping the core values of helping to reduce eye strain intacts but getting some contrast in relation to help programmers, students or whoever may benefit to better manage their time and make the most of their time by making some custom reminders. I personally worked with several different approaches on this project making it pretty simple non-userfrindly at all and 100% python based in order to make those reminders to interact with my WLS-2 terminal and play those messages, but I alway wanted to make it user-friendly with some user interfaces so anyone with non programming knoledge whatsoever could use it and benefit the most from it, so making this project based on something I wanted do since I started my programming jurney has been really fulfilling.

#### Project development process and it's challenges:
First of all I had to question my self about what my current knoledge was at the starting stage of this project. The only thing that I knew was that I was quite proficient with python, I had learned some JavaScript and SQL thanks to CS50x. Whoever I felt like that wasn't quite enough since I wanted to make a real project that could, at some point, getting deployed. Make it modular and easily scalable was a priority, I already knew a little bit of Flask, but that was still not what I wanted. I loved some much CS50x and I saw there was a curse called CS50w focused on web development so thats when I found django. CS50w was greatly helpful in order to get a deeper knoledge about what I already had an small idea, so that was when at that point I decided to watch the lectures from 0 to 5 covering HTML, CSS, Git, Python, SQL and specially the django Models and a little dive deeper into JavaScript.

I was taking the new knoledge and implementing simultaneusly on the go, mixing everying I was learning on real time. Puting the ideas on paper and structure all the different nav taps the projec would have was pretty usefull too. The hardest part of this project was when I had the idea of storaging the greetings from the users, an audio file is such an heavy weight and I wasnt even aware if storaging audio files in a database was even possible. I was thinking on developing a back-end process where the user entered the text, then via POST getting user input and use the text-to-speech generator from google called gTTs, then storage that .wav file some how to the database. During my research I found the file systems and that was something else I did knew too. After a coulpe of days of focusing into the smaller parts of this project, an idea came to my mind and that was canonic moment for me and this project. What if instead of storaging such complicated thing I just storage the greeting in the form of text? Thats when I tried modifying the python text-to-speech generator to instead of storaging the file itself just its version in memory then playing it and forgetting about it. That was still quite inefficient. So many server-side processes and requests to handle. So then when I saw the last part of the lesson 5 at CS50w course I found the concept of APIs, a little research and quickly found out and API which is widely supported by most of the browsers and a browser-side process that would just make everything way more clean, simple and efficient. That was how finally this project took its direction and was compleated after more than 12 days of hard work, coding and working on it for more than 12 hours per day in average. I had to learn so much more about HTML, CSS, JS, Python, and even get used to Django, learning it completly from scratch for this project.

#### Content: Describe each of the files I wrote what contains and does, debate design choises

/venvTimer-Look_away
During the research process, before starting the project I read about good practices and I found out about using virtual enviroments when working with python, actually just as a coincidence I run in troubles using my new python version because I updated and that was when the virtual enviroment actually came in handy

/requirements.txt
By runnnig: pip freeze > requirements.txt the requirements files is generated, containing all the packages needed in order to run this project
So it can be easily run just by executing: pip install -r requirements.txt
In this way this project should work properly in any machine

/timerMain
The main file of this project, where another apps can be inserted. the timerApp is inside of it. As its main files that are storaged inside of it where I made some set up updates are the settings.py where I added to the INSTALLED_APPS = [] the timerApp. Include in the main urls path the app by adding the timerApp to the urlpatterns.

/timerMain/timerApp
The main app repository of this project where all the files are storaged. The static files, templates and python files that are part of the Model View Controller. Each of these will be reviewed in detail bellow:

/timerMain/timerApp/static/timerApp
The static templates include:

The image that was set as background image.
The styles sheet including all the css properties that were set for the different templates of this project
Two JavaScript files. The main JavaScript file (timercountdown.js) for the project which is only accessible by registered users, displaying a count down timer to show up how much time is left until the reminder will be played back. And a simplified version of itself just for the trial version for the objective public who havent sing up yet.

/timerMain/timerApp/templates/timerApp
All the diferent templates which are the building blocks of the website, every feature thats available for this app, the index and home page, the main layout which  gives the structure to our templates, login, sign up, password update, login, trial and the timers page.

/timerMain/timerApp/views.py
The back-end or server-side implementation of every function, handaling server-side input verification and rendering the html pages

/timerMain/timerApp/urls.py
Is the URL dispatcher or scheme serving as a mapping between the url and the views

/timerMain/timerApp/models.py
Serving as the database of this project, where the timers input is storaged. Linking the timer to it's respective user, setting a name for the timer, a speech greeting text, the interval duration of the timer and the timer's creation date

/timerMain/timerApp/functions.py
I created it to keep views.py clean and readable and improve modularity.

/timerMain/timerApp/admin.py
added the Model to the admin site in order to be able to delete and manage users and timers during the development.

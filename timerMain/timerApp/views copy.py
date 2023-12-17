from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .functions import signup_validation, timer_validation
from .models import Timer

# Create your views here.
def index(request):
    return render(request, 'timerApp/index.html')


def trial(request):
    return render(request, 'timerApp/trial.html')


def signup(request):

    if request.method == "POST":

        # Get form information
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Call function to validate input and return True and intro messages if successful or False and error message if not
        output = signup_validation(username, email, password, confirmation)

        # if function returned true
        if output[0] == True:
            # Create new user
            user = User.objects.create_user(username, email, password)
            # Add demo timer and intro message
            add_demo = Timer.objects.create(user=user, name=output[1], interval=1, message=output[2])
            login(request, user)
            return render(request, "timerApp/home.html", {"message": f"Thanks for joining {username.capitalize()}!, I hope you enjoy the app!"})
        
        elif output[0] == False:
            # The function returned a message
            return render(request, "timerApp/signup.html", {"message": output[1]})

    else:
        return render(request, "timerApp/signup.html")


def login_view(request):

    if request.method == "POST":

        # Get form information
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if any fields are empty
        if not username or not password:
            return render(request, "timerApp/login.html", {
                "message": "All fields must be filled out."
            })
        
        # Check if username and password are correct
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # Login user
            login(request, user)
            return render(request, "timerApp/home.html", {"message": f"Welcome, {username.capitalize()}!!"})

        else:
            return render(request, 'timerApp/login.html', {
                "message": "Invalid credentials"
            })
        
    # If user is not logged in, redirect to login page
    return render(request, 'timerApp/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'timerApp/index.html', {
        "message": "Logged out."
    })


@login_required(login_url='timerApp:login')
def home(request):
    return render(request, 'timerApp/home.html')


@login_required(login_url='timerApp:login')   
def timers(request):
    
    if request.method == "POST":
        # Get form information
        name = request.POST["timerName"]
        minutes = request.POST["timerMinutes"]
        hours = request.POST["timerHours"]
        message = request.POST["timerSpeech"]
        
        # Get user information
        user = request.user

        # Get all timers associated with the user
        timers = user.timers.all()

        output = timer_validation(name, minutes, hours, message, timers)
        
        # if function returned true
        if output == True:
            # Create new timer
            set_timer = Timer.objects.create(user=user, name=name, interval=int(minutes) + int(hours) * 60, message=message)
            return render(request, 'timerApp/home.html', {"message": f"Timer {name} created!"})
        elif output[0] == False:
            # Function returned an error message
            return render(request, "timerApp/timers.html", {"message": output[1]})    

    return render(request, 'timerApp/timers.html')

@login_required(login_url='timerApp:login')
def speech(request):
    return render(request, 'timerApp/speech.html')



# Change password
@login_required(login_url='timerApp:login')
def password(request):

    if request.method == "POST":
        # Get form information
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirmation = request.POST["confirmation"]

        # Check if any fields are empty
        if not request.POST["old_password"] or not request.POST["new_password"] or not request.POST["confirmation"]:
            return render(request, "timerApp/password.html", {"message": "All fields must be filled out."})

        # Ensure old password is correct
        pw_check = authenticate(request, username=request.user.username, password=request.POST["old_password"])
        
        if pw_check is None:
            return render(request, "timerApp/password.html", {"message": "Incorrect password."})

        # Check if passowords match
        elif request.POST["new_password"] != request.POST["confirmation"]:
            return render(request, "timerApp/password.html", {"message": "Passwords don't match."})

        # make sure password is at least 6 characters
        elif len(request.POST["new_password"]) < 6:
            return render(request, "timerApp/password.html", {"message": "Password must be at least 6 characters."})
         
        # Change password
        user = User.objects.get(username=request.user.username)
        user.set_password(request.POST["new_password"])
        user.save()
        return render(request, "timerApp/home.html", {"message": "Password successfully updated!"})

    else:
        return render(request, "timerApp/password.html")
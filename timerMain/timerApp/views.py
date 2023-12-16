from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render

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

        # input validation

        # Check if any fiels are empty
        if not username or not email or not password or not confirmation:
            return render(request, "timerApp/signup.html", {"message": "All fields must be filled out.."})

        # Check if username or email already exists
        elif User.objects.filter(username=username).exists():
            return render(request, "timerApp/signup.html", {"message": "Username already taken."})

        elif User.objects.filter(email=email).exists():
            return render(request, "timerApp/signup.html", {"message": "Email already in use."})
        
        # Check if username and password are valid
        elif len(username) < 5 or len(username) > 64:
            return render(request, "timerApp/signup.html", {"message": "Username must be between 5 and 64 characters."})
        
        elif len(password) < 6:
            return render(request, "timerApp/signup.html", {"message": "Password must be at least 6 characters."})
        
        # Check if passwords match
        elif password != confirmation:
            return render(request, "timerApp/signup.html", {"message": "Passwords must match."})

        # Create new user
        user = User.objects.create_user(username, email, password)

        # Add demo timer and intro message
        message = f"Hello {user.username}! Welcome to Timer Look Away! This is a demo timer! Make the most of your time, thanks to Timer Look Away!"
        if len(message) > 128:
            message = f"Hello {user.username}! Welcome to Timer Look Away! Make the most of your time!"
        
        name = f"Demo Timer; Welcome {user.username} to TLA!"
        if len(name) > 64:
            name = f"Demo Timer, Welcome to TLA!"

        add_demo = Timer.objects.create(user=user, name=name, interval=1, message=message)

        login(request, user)
        
        return render(request, "timerApp/home.html", {"message": f"Thanks for joining {username.capitalize()}!, I hope you enjoy the app!"})
        
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

        # Check if any fields are empty
        if not name or not message or not minutes or not hours:
            return render(request, "timerApp/timers.html", {"message": "All fields must be filled out."})
        
        # Check if timer name or speech message already exists
        # Load conditional results into variables to avoid multiple database calls
        name_exists = timers.filter(name=name).exists()
        message_exists = timers.filter(message=message).exists()
        
        if name_exists or message_exists:
            if name_exists:
                return render(request, "timerApp/timers.html", {"message": "Timer name already exists."})
            else:
                return render(request, "timerApp/timers.html", {"message": "Speech message already exists."})

        # Check if timer name and speech is valid
        elif len(name) > 64 or len(message) > 128:
            if len(name) > 64:
                return render(request, "timerApp/timers.html", {"message": "Timer name must be less than 64 characters."})
            else:
                return render(request, "timerApp/timers.html", {"message": "Speech message must be less than 128 characters."})
            
        # Check if minutes and hours are valid
        elif not minutes.isdigit() or not hours.isdigit():
            return render(request, "timerApp/timers.html", {"message": "Minutes and hours must be numbers."})
        
        # Check if minutes and hours are within range
        elif int(minutes) > 59 or int(hours) > 15:
            return render(request, "timerApp/timers.html", {"message": "Minutes must be less than 60 and hours must be less than 16."})

        # make sure timer is at least 1 minute
        elif int(minutes) + int(hours) * 60 < 1:
            return render(request, "timerApp/timers.html", {"message": "Timer must be at least 1 minute."})
        
        # Create new timer
        set_timer = Timer.objects.create(user=user, name=name, interval=int(minutes) + int(hours) * 60, message=message)

        return render(request, 'timerApp/home.html', {
            "message": f"Timer {name} created!"})

    return render(request, 'timerApp/timers.html')

@login_required(login_url='timerApp:login')
def speech(request):
    return render(request, 'timerApp/speech.html')



# Change password
@login_required(login_url='timerApp:login')
def password(request):

    if request.method == "POST":

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
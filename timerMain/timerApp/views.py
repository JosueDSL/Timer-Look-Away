from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
import json

# Fuctions.py was created to keep views.py clean and readable and improve modularity. 
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
            request.session['message'] = f"Thanks for joining {username.capitalize()}! I hope you enjoy the app!"
            return redirect('timerApp:home')
        
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
            request.session['message'] = f"Welcome, {username.capitalize()}!!"
            return redirect('timerApp:home')

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

# Create a view to serialize timers to json and call it from javascript as an API
@login_required(login_url='timerApp:login')
def get_timersjson(request):
    # Get user information
    user = request.user
    # Get all timers associated with the user
    timers = user.timers.all()
    timer_json = serializers.serialize('json', timers)
    return JsonResponse(json.loads(timer_json), safe=False)


@login_required(login_url='timerApp:login')
def home(request):
    
    if request.method == "POST":
        # Get form information

        return render(request, 'timerApp/home.html', {"message": "POST request received"})

    else:
        # Get user information
        user = request.user

        # Get all timers associated with the user
        timers = user.timers.all()
        # Check if there is a message in the session
        message = request.session.get('message', '')
        
        if 'message' in request.session:
            del request.session['message']
            return render(request, 'timerApp/home.html', {"message": message, "timers": timers })
        
        return render(request, 'timerApp/home.html', {"timers": timers})


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
            request.session['message'] = f"Timer {name} successfully created!"
            return redirect('timerApp:home')
        
        elif output[0] == False:
            # Function returned an error message
            return render(request, "timerApp/timers.html", {"message": output[1]})    

    return render(request, 'timerApp/timers.html')

def delete_timer(request, timer_id):
    if request.method == "POST":
        # Make sure the timer id belongs to the user
        user = request.user
        timer = Timer.objects.get(id=timer_id)
        
        if timer.user != user:
            request.session['message'] = "You can't delete that timer."
            return redirect('timerApp:home')
        
        # Delete timer
        user.timers.filter(id=timer_id).delete()
        request.session['message'] = "Timer successfully deleted."
        return redirect('timerApp:home')

# Change password
@login_required(login_url='timerApp:login')
def password(request):

    if request.method == "POST":
        # Get form information
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirmation = request.POST["confirmation"]

        # Check if any fields are empty
        if not old_password or not new_password or not confirmation:
            return render(request, "timerApp/password.html", {"message": "All fields must be filled out."})

        # Ensure old password is correct
        pw_check = authenticate(request, username=request.user.username, password=request.POST["old_password"])
        
        if pw_check is None:
            return render(request, "timerApp/password.html", {"message": "Incorrect password."})

        # Check if passowords match
        elif new_password != confirmation:
            return render(request, "timerApp/password.html", {"message": "Passwords don't match."})

        # make sure password is at least 6 characters
        elif len(new_password) < 6:
            return render(request, "timerApp/password.html", {"message": "Password must be at least 6 characters."})
         
        # Change password
        user = User.objects.get(username=request.user.username)
        user.set_password(new_password)
        user.save()
        
        # Authenticate user to redirect to home page
        user_authentication = authenticate(request, username = user, password = new_password)
        if user_authentication is not None:
            # Login user
            login(request, user_authentication)
            request.session['message'] = "Password successfully updated!"
            return redirect('timerApp:home')

    else:
        return render(request, "timerApp/password.html")
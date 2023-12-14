from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render

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
        if User.objects.filter(username=username).exists():
            return render(request, "timerApp/signup.html", {"message": "Username already taken."})

        elif User.objects.filter(email=email).exists():
            return render(request, "timerApp/signup.html", {"message": "Email already in use."})
        
        # Check if username and password are valid
        elif len(username) < 5:
            return render(request, "timerApp/signup.html", {"message": "Username must be at least 5 characters."})
        elif len(password) < 6:
            return render(request, "timerApp/signup.html", {"message": "Password must be at least 6 characters."})
        
        # Check if passwords match
        if password != confirmation:
            return render(request, "timerApp/signup.html", {"message": "Passwords must match."})

        # Create new user
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse("timerApp:index"))
        
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
    pass

@login_required(login_url='timerApp:login')
def speech(request):
    pass



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
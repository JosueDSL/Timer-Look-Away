from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'timerApp/home.html')


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("timerApp:login"))
    
    else:
        return render(request, 'timerApp/home.html')


def trial(request):
    return render(request, 'timerApp/trial.html')


def signup(request):

    if request.method == "POST":

        # Get form information
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Check if any fiels are empty
        if not username or not email or not password or not confirmation:
            return render(request, "register.html", {"message": "All fields must be filled out.."})

        # Check if passwords match
        if password != confirmation:
            return render(request, "register.html", {"message": "Passwords must match."})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"message": "Username already taken."})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"message": "Email already in use."})

        # Create new user
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect("index")
        
    else:
        return render(request, "timerApp/signup.html")

    
def timers(request):
    pass

def speech(request):
    pass

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
            return HttpResponseRedirect(reverse("timerApp:index"))

        else:
            return render(request, 'timerApp/login.html', {
                "message": "Invalid credentials"
            })
        
    # If user is not logged in, redirect to login page
    return render(request, 'timerApp/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'timerApp/login.html', {
        "message": "Logged out."
    })

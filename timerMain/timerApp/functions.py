from django.shortcuts import render
from django.contrib.auth.models import User


def signup_validation(username, email, password, confirmation):
        
        # Check if any fiels are empty
        if not username or not email or not password or not confirmation:
             error_message = "All fields must be filled out"
             return False, error_message
        
        # Check if username or email already exists
        elif User.objects.filter(username=username).exists():
            error_message = "Username already taken."

        elif User.objects.filter(email=email).exists():
            error_message = "Email already in use."
            return False, error_message
        # Check if username and password are valid
        elif len(username) < 5 or len(username) > 64:
            error_message = "Username must be between 5 and 64 characters."
            return False, error_message
        elif len(password) < 6:
            error_message = "Password must be at least 6 characters."
            return False, error_message
        # Check if passwords match
        elif password != confirmation:
            error_message = "Passwords must match."
            return False, error_message

        # Create two intro name and message based on username length
        intro_message = f"Hello {username}! Welcome to Timer Look Away! This is a demo timer! Make the most of your time, thanks to Timer Look Away!"
        if len(intro_message) > 128:
            intro_message = f"Hello {username}! Welcome to Timer Look Away! Make the most of your time!"
        
        intro_name = f"Demo Timer; Welcome {username} to TLA!"
        if len(intro_name) > 64:
            intro_name = f"Demo Timer, Welcome to TLA!"

        return True, intro_name, intro_message

def timer_validation(name, minutes, hours, message, timers):
          
        # Check if any fields are empty
        if not name or not message or not minutes or not hours:
            error_message = "All fields must be filled out."
            return False, error_message
        print(minutes)
        # Check if timer name or speech message already exists
        # Load conditional results into variables to avoid multiple database calls
        name_exists = timers.filter(name=name).exists()
        message_exists = timers.filter(message=message).exists()
        
        if name_exists or message_exists:
            if name_exists:
                error_message = "Timer name already exists."
                return False, error_message
            else:
                error_message = "Speech message already exists."
                return False, error_message

        # Check if timer name and speech is valid
        elif len(name) > 64 or len(message) > 128:
            if len(name) > 64:
                error_message = "Timer name must be less than 64 characters."
                return False, error_message
            else:
                error_message = "Speech message must be less than 128 characters."
                return False, error_message
            
        # Check if minutes and hours are valid
        elif not minutes.isdigit() or not hours.isdigit():
            error_message = "Minutes and hours must be numbers."
            return False, error_message
        
        # Check if minutes and hours are within range
        elif int(minutes) > 60 or int(hours) > 15:
            error_message = "Minutes must be less than 60 and hours must be less than 16."
            return False, error_message
        
        # make sure timer is at least 1 minute
        elif int(minutes) < 1:
            error_message = "Timer must be at least 1 minute."
            return False, error_message
        
        return True
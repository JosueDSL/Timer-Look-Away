import time
import pygame

class LoadSound:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            # Attempt to open the file
            pygame.mixer.init()
            sound = pygame.mixer.Sound(self.filename)
            return sound
        except pygame.error:
            # File not found in the current directory
            print('File not found')

class Timer:
    def __init__(self, interval):
        self.interval = interval
        self.counter = 0

    def tick(self):
        self.counter += 60

    def reset(self):
        self.counter = 0

look_sound = LoadSound("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/pjet-organization/look_away.wav").load()
break_sound = LoadSound("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/pjet-organization/take-a-break.wav").load()

look_away = Timer(15 * 60)  # 15 minutes in seconds
take_a_break = Timer(2 * 60 * 60)  # 2 hours in seconds

while True:

    if take_a_break.counter >= take_a_break.interval:
        look_away.reset()        
        with open("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/pjet-organization/time_check.txt", "a") as file:
            update = file.write("Break 2H Played at: " + time.strftime("%H:%M:%S") + "\n")
        take_a_break.reset()
        if break_sound:
            break_sound.play()
        else:
            print("No sound file found")
    
    if look_away.counter >= look_away.interval:
        with open("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/pjet-organization/time_check.txt", "a") as file:
            update = file.write("LA 15M Played at: " + time.strftime("%H:%M:%S") + "\n")
        look_away.reset()
        if look_sound:
            look_sound.play()
        else:
            print("No look away sound file found")

    time.sleep(60)
    look_away.tick()
    take_a_break.tick()
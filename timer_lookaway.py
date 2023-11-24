import time
import simpleaudio as sa

class LoadSound:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            # Attempt to open the file
            audio_file = sa.WaveObject.from_wave_file(self.filename)
            return audio_file
        except FileNotFoundError:
            # What to do if the file was not found
            print('File not found')

class Timer:
    def __init__(self, interval):
        self.interval = interval
        self.counter = 0

    def tick(self):
        self.counter += 60

    def reset(self):
        self.counter = 0

wave_obj = LoadSound("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/look_away.wav").load()
wave_obj2 = LoadSound("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/take-a-break.wav").load()

look_away = Timer(15 * 60)  # 15 minutes in seconds
take_a_break = Timer(2 * 60 * 60)  # 2 hours in seconds

while True:
    
    if look_away.counter >= look_away.interval:
        with open("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/time_check.txt", "a") as file:
            update = file.write("LA 15M Played at: " + time.strftime("%H:%M:%S") + "\n")
        look_away.reset()
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if take_a_break.counter >= take_a_break.interval:
        with open("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/time_check.txt", "a") as file:
            update = file.write("Break 2H Played at: " + time.strftime("%H:%M:%S") + "\n")
        take_a_break.reset()
        play_obj2 = wave_obj2.play()
        play_obj2.wait_done()

    time.sleep(60)
    look_away.tick()
    take_a_break.tick()
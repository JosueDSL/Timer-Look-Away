import time
import simpleaudio as sa

class Timer:
    def __init__(self, interval):
        self.interval = interval
        self.counter = 0

    def tick(self):
        self.counter += 60

    def reset(self):
        self.counter = 0

wave_obj = sa.WaveObject.from_wave_file("look_away.wav")
wave_obj2 = sa.WaveObject.from_wave_file("take-a-break.wav")

look_away = Timer(15 * 60)  # 15 minutes in seconds
take_a_break = Timer(2 * 60 * 60)  # 2 hours in seconds

while True:
    
    if look_away.counter >= look_away.interval:
        look_away.reset()
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if take_a_break.counter >= take_a_break.interval:
        take_a_break.reset()
        play_obj2 = wave_obj2.play()
        play_obj2.wait_done()

    time.sleep(60)
    look_away.tick()
    take_a_break.tick()
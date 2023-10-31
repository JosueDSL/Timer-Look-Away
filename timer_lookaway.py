import time
import simpleaudio as sa
import psutil

import time
import simpleaudio as sa
import psutil

wave_obj = sa.WaveObject.from_wave_file("look_away.wav")
wave_obj2 = sa.WaveObject.from_wave_file("take-a-break.wav")

look_away_interval = 15 * 60  # 15 minutes in seconds
take_a_break_interval = 2 * 60 * 60  # 2 hours in seconds

look_away_last_played = time.time()
take_a_break_last_played = time.time()

while True:
    current_time = time.time()
    time_difference = current_time - look_away_last_played
    
    if time_difference >= look_away_interval:
        with open("/home/joxulds/Enviroment-Setup/Personalization/Timer-Look-Away/memory_usage.txt", "a") as f:
            f.write(f"Memory usage: {psutil.virtual_memory().used/1024/1024:.2f} MB\n")
        look_away_last_played = current_time
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if current_time - take_a_break_last_played >= take_a_break_interval:
        take_a_break_last_played = current_time
        play_obj2 = wave_obj2.play()
        play_obj2.wait_done()

    time.sleep(60)

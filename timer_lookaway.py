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
    if time.time() - look_away_last_played >= look_away_interval:
        play_obj = wave_obj.play()
        play_obj.wait_done()
        look_away_last_played += look_away_interval
    
    if time.time() - take_a_break_last_played >= take_a_break_interval:
        play_obj2 = wave_obj2.play()
        play_obj2.wait_done()
        take_a_break_last_played += take_a_break_interval
    
    if time.time() - look_away_last_played >= 15 * 60:
        with open("memory_usage.txt", "a") as f:
            f.write(f"Memory usage: {psutil.virtual_memory().percent}%\n")
    
    time.sleep(60)

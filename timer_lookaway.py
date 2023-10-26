import time
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("look_away.wav")

while True:
    play_obj = wave_obj.play()
    play_obj.wait_done()
    time.sleep(600) 
from gtts import gTTS
from pydub import AudioSegment

# Save the file with gTTS
tts = gTTS('Hey! Josh!, Remember to take a break, its been 2 hours already!', lang='en')
tts.save('take-a-break.mp3')

#Convert the file to WAV with pydub
sound = AudioSegment.from_mp3('take-a-break.mp3')
sound.export('take-a-break.wav', format='wav')
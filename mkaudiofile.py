from gtts import gTTS
from pydub import AudioSegment

# Save the file with gTTS
tts = gTTS('Hey! Josh!, look away from the screen', lang='en')
tts.save('look_away.mp3')

#Convert the file to WAV with pydub
sound = AudioSegment.from_mp3('look_away.mp3')
sound.export('look_away.wav', format='wav') 
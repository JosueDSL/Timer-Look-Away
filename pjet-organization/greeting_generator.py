from gtts import gTTS
from pydub import AudioSegment

# Save the file with gTTS
tts = gTTS('Timer Look Away Successfully started!', lang='en')
tts.save('take-a-break.mp3')

#Convert the file to WAV with pydub
sound = AudioSegment.from_mp3('take-a-break.mp3')
sound.export('Notification_started.wav', format='wav')
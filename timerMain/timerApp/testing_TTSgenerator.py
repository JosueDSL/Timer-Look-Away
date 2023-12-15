from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')

    # Save gTTS to BytesIO
    mp3_data = io.BytesIO()
    tts.write_to_fp(mp3_data)
    mp3_data.seek(0)

    # Convert BytesIO to AudioSegment
    audio = AudioSegment.from_file(mp3_data, format="mp3")

    # Play the audio
    play(audio)

# Example usage
text = "Hey Josh, remember to look away!, it's been 2 hours already!"
text_to_speech(text)
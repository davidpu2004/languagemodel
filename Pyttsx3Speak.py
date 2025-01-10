
import pyttsx3
from pyttsx3.voice import Voice

class Pyttsx3Speak:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        # volume = engine.getProperty('volume')
        # engine.setProperty('volume', volume + 0.50)
        for voice in self.engine.getProperty('voices'):
            print(f"Voice: {voice.name} (ID: {voice.id}) ")

    def get_chinese_voice(self) -> Voice:
        # chinese voice: "zh-CN"
        for voice in self.engine.getProperty("voices"):
            if voice.languages and voice.languages[0] == "zh-CN":
                return voice
            if "Chinese" in voice.name or "Mandarin" in voice.name.title():
                return voice
        raise RuntimeError(f"No Chinese voice found among {self.engine.getProperty('voices')}")

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    pytts = Pyttsx3Speak()
    text1 = "Historical items hidden for decades have been uncovered in the crypts of a cathedral in Lithuania"
    text2="including burial crowns and insignia belonging to medieval rulers. Some of them haven’t been seen since World War II broke out in 1939"
    pytts.speak(text1)
    pytts.speak(text2)

if __name__ == "__main__":
        main()
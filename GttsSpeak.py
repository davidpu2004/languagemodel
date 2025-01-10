
from gtts import gTTS
import gtts.lang
import os

class GttsSpeak:
    def __init__(self, lang):
        # chinese: lang='zh-CN'
       self.lang=lang
       print(gtts.lang.tts_langs())

    def speak(self,text):
        tts = gTTS(text=text, lang=self.lang)
        tts.save("pcvoice.mp3")
        os.system("start pcvoice.mp3")

def main():
    gtts = GttsSpeak('zh-CN')
    text = "法新社报导，奥班在国情咨文演说中表示，“好消息是，目前我们与瑞典的争端正走向终点。我们与瑞典总理共同采取了重要步骤，以重建信任”，但他并未说明细节"
    gtts.speak(text)

if __name__ == "__main__":
        main()
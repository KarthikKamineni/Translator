import googletrans
import os
from gtts import gTTS
from gtts.lang import tts_langs
from music import get_music_player
from utils import create_popup

import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty


kivy.require("2.1.0")


class Translator(AnchorLayout):
    lang = ObjectProperty(None)
    text_in = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prev = ""
        self.lang.values = self.get_lang().values()
        self.t = googletrans.Translator()
        self.player = get_music_player()

    def speak(self):
        try:
            if self.text_in.text.strip() != "":
                text = self.t.translate(self.text_in.text, self.lang.text).text
                if self.prev != text.strip():
                    if os.path.exists("c_v.mp3"):
                        os.remove("c_v.mp3")
                    gTTS(text, lang=googletrans.LANGCODES[self.lang.text.lower()]).save("c_v.mp3")
                self.player.reset()
                self.player.load("c_v.mp3")
                self.player.play()
                self.prev = text.strip()
            else:
                create_popup(context="Text Cannot be empty.")
        except Exception as e:
            create_popup(context=str(e))

    def get_lang(self):
        try:
            d1 = googletrans.LANGUAGES
            d2 = tts_langs()
            common_lang_codes = dict()
            for k in d2:
                if k in d1:
                    common_lang_codes[k] = d2[k]
            return common_lang_codes
        except Exception as e:
            create_popup(context=str(e))


class MainApp(App):
    def build(self):
        return Translator()


if __name__ == "__main__":
    MainApp().run()

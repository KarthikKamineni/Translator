from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty



class PopUI(BoxLayout):
    c_text=ObjectProperty(None)
    def __init__(self,c_text,popup,**kwargs):
        super().__init__(**kwargs)
        self.c_text.text=c_text
        self.popup=popup
    def close(self):
        self.popup.dismiss()



def create_popup(title="Error",context="..something...",**kwargs):
    popup=Popup(title=title,auto_dismiss=False,size_hint=(1,.5),**kwargs)
    popup.content=PopUI(context,popup)
    popup.open()
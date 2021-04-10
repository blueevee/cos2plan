from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400,600)

class MainScreen(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Test(MDApp):
    def build(self):
        return MainScreen()

Test().run()
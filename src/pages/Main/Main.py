from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout, MDAdaptiveWidget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView

Window.size = (400,600)

class MyScreenManager(ScreenManager):
    pass

class MainScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class NewCosplayScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def show_data(self, name, origin, budget, url):
        print([name, origin, budget, url])

class Test(MDApp):
    def build(self):
        return MyScreenManager()

Test().run()
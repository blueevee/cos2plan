from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.card import MDCardSwipe

Window.size = (400,600)

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()

class MainScreen(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return self.screen

    def on_swipe_complete(self, instance):
        self.screen.ids.md_list.remove_widget(instance)

    def on_start(self):
        for i in range(20):
            self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )


class Test(MDApp):
    def build(self):
        return MainScreen()

Test().run()
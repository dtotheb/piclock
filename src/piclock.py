from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

import screens
import navbars

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '240')

presentation = Builder.load_file("piclock.kv")

class ClockRoot(BoxLayout):
    screen_man = ObjectProperty()

class PiClockApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    PiClockApp().run()

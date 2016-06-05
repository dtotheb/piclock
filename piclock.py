from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


import time
from subprocess import *

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '240')

ip_cmd = "ip addr show wlan0 | grep -w inet | awk '{print $2}' | cut -d/ -f1"
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

class MainScreen(Screen):
    pass

class ClockScreen(Screen):
    current_time = ObjectProperty()

    def updateTime(self, dt):
        self.current_time.text = time.strftime("%I:%M:%S %p", time.localtime())

class StatusScreen(Screen):
    ip_address = ObjectProperty()


    def updateStatus(self, dt):
        self.ip_address.text = run_cmd(ip_cmd)




class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("piclock.kv")

class PiClockApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    PiClockApp().run()

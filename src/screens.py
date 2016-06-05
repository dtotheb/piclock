from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


import time
from subprocess import *

ip_cmd = "ip addr show wlan0 | grep -w inet | awk '{print $2}' | cut -d/ -f1"
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output


class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class ClockScreen(Screen):
    current_time = ObjectProperty()

    def updateTime(self, dt):
        self.current_time.text = time.strftime("%I:%M:%S %p", time.localtime())

class StatusScreen(Screen):
    ip_address = ObjectProperty()


    def updateStatus(self, dt):
        #self.ip_address.text = run_cmd(ip_cmd)
        pass

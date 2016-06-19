from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('screens.kv')

import time
from subprocess import *

ip_cmd = "ip addr show wlan0 | grep -w inet | awk '{print $2}' | cut -d/ -f1"
cputemp_cmd = 'vcgencmd measure_temp'
uptime_cmd = 'uptime -p'


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0].rstrip()
    return output


def getIPaddress():
    return run_cmd(ip_cmd)



def getCPUtemperature():
    res = run_cmd(cputemp_cmd)
    return(res.replace("temp=","").replace("'C\n",""))

def getUptime():
    res = run_cmd(uptime_cmd)
    return(res.replace("up ",""))



class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class ClockScreen(Screen):
    current_time = ObjectProperty()

    def setupClockScreen(self):
        Clock.schedule_interval(self.updateTime, 0.01)

    def updateTime(self, dt):
        self.current_time.text = time.strftime("%I:%M:%S", time.localtime())

class StatusScreen(Screen):
    ip = ObjectProperty()
    cuptemp = ObjectProperty()
    uptime = ObjectProperty()

    def setupStatusScreen(self):
        self.updateStatus(0.1)
        Clock.schedule_interval(self.updateStatus, 1)

    def updateStatus(self, dt):
        self.ip.text = getIPaddress()
        self.cputemp.text = getCPUtemperature()
        self.uptime.text = getUptime()

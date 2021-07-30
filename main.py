import csv
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.widget import Widget

from modules import shibo
from modules import toGoogle

resource_add_path("./fonts/")
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


c = shibo.ShiftContainer(dataString)
event_dicts = c.dataDicts
c.toGoogleCSV()


class LoadCalendar(Widget):
    def googleBotton(self):
        toGoogle.setEvent(event_dicts)



class ShiboApp(App):
    pass

ShiboApp().run()


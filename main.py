import csv
from kivy.app import App
from kivy.uix.button import Button

from modules import shibo
from modules import toGoogle

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


c = shibo.ShiftContainer(dataString)
event_dicts = c.dataDicts
c.toGoogleCSV()

class ShiboApp(App):
    pass

ShiboApp().run()


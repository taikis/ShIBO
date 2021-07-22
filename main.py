import csv

from modules import shibo
from modules import toGoogle

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


c = shibo.ShiftContainer(dataString)
event_dicts = c.dataDicts
c.toGoogleCSV()
toGoogle.createEvent(event_dicts,toGoogle.getCalenderId())
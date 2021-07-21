import csv

from my import shibo

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


c = shibo.ShiftContainer(dataString)
c.toGoogleCSV()
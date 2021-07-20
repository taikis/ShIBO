import csv

outputPath = "./output/shft.csv"

with open(outputPath,'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Subject","Start Date","Start Time","End Date","End Time"])


inputPath = "./data/shift.txt"
with open(inputPath,'r') as f:
    dataString = f.read()



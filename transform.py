import csv

outputPath = "./output/shft.csv"

with open(filepath + filename,'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Subject","Start Date","Start Time","End Date","End Time"])

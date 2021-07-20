import csv
import datetime

outputPath = "./output/shft.csv"

with open(outputPath, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(
        ["Subject", "Start Date", "Start Time", "End Date", "End Time"])

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


class formatter:
    def __init__(self, dataString):
        self.dataDicts = []
        dataArray = dataString.splitlines()
        
    @staticmethod
    def setDate(month,day,hour,minite):
        '''
        日付を入れると今日以降の年を推定する

        Parameters
        -----------
        month : str
            月
        day : str
            日
        hour : str
            hh形式の時間
        minite : str
            mm形式の分
        
        Returns
        ------------
        date : datetime
            datetime形式の年が調整された日付
        '''

        today = datetime.datetime.now()
        year = today.year
        month = int(month)
        hour = int(hour)
        minite = int(minite)
        day = int(day)
        if(month < today.month):
            year += 1
        date = datetime.datetime(year,month,day,hour,minite)
        return date



c = formatter(dataString)

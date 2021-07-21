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
        self.parseData([dataArray[0],dataArray[1]])
        self.dataDicts.append(self.parseData([dataArray[0],dataArray[1]]))

    def parseData(self, dataString):
        '''データを一回分もらい、辞書形式に直して渡す

        Parameters
        ----------
        dataString : String
            一回分のデータ
            最初の列に日付、次の列にバイト先の名前が入っている

        Returns
        -------
        dict[str,datetime,datetime]
            バイト先の名前、始まりの時間、終わりの時間
        '''
        dataDict = {}
        dataDict["startDate"] = self.setDate(dataString[0][0:2],dataString[0][3:5],dataString[0][8:10],dataString[0][11:13])
        dataDict["endDate"] = self.setDate(dataString[0][0:2],dataString[0][3:5],dataString[0][16:18],dataString[0][19:21])
        dataDict["subject"] = dataString[1][2:]
        return dataDict
    
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

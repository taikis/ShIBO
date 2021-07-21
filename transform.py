import csv
import datetime
import re

outputPath = "./output/shft.csv"

with open(outputPath, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(
        ["Subject", "Start Date", "Start Time", "End Date", "End Time"])

inputPath = "./data/shift.txt"
with open(inputPath, 'r') as f:
    dataString = f.read()


class Formatter:
    def __init__(self, dataString):
        self.dataDicts = []
        dataArray = dataString.splitlines()
        self.parseData([dataArray[0],dataArray[1]])
        self.dataDicts.append(self.parseData([dataArray[0],dataArray[1]]))
    
    def checkData(self,dataString):
        '''それがシフトボードから出力されたデータなのかを正規表現を用いてチェックする

        Parameters
        ----------
        dataString : String
            文字列データの一行分

        Returns
        -------
        int
            データかどうか
            0 : データではない
            1 : 時間データである
            2 : バイト先データである
            3 : 何もない
            4 : 最終行のデータである
        '''

        NOT_SHIFT_DATA = 0
        TIME_DATA = 1
        SUBJECT_DATA = 2
        NO_DATA = 3
        END_LINE = 4
        stateData = NOT_SHIFT_DATA
        
        timeRe = re.compile("\d{2}/\d{2}（(月|火|水|木|金|土|日)）\d{2}:\d{2}\s-\s\d{2}:\d{2}")
        subRe = re.compile("-\s.+")

        if timeRe.fullmatch(dataString) is not None:
            stateData = TIME_DATA
        elif subRe.fullmatch(dataString) is not None:
            stateData = SUBJECT_DATA
        elif len(dataString) == 0:
            stateData = NO_DATA
        elif dataString == "シフト管理アプリ「シフトボード」で作成":
            stateData = END_LINE

        return stateData

        


    def parseData(self, dataStrings):
        '''データを一回分もらい、辞書形式に直して渡す

        Parameters
        ----------
        dataStrings : String
            一回分のデータ
            最初の列に日付、次の列にバイト先の名前が入っている

        Returns
        -------
        dict[str,datetime,datetime]
            バイト先の名前、始まりの時間、終わりの時間
        '''
        dataDict = {}
        dataDict["startDate"] = self.setDate(dataStrings[0][0:2],dataStrings[0][3:5],dataStrings[0][8:10],dataStrings[0][11:13])
        dataDict["endDate"] = self.setDate(dataStrings[0][0:2],dataStrings[0][3:5],dataStrings[0][16:18],dataStrings[0][19:21])
        dataDict["subject"] = dataStrings[1][2:]
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



c = Formatter(dataString)

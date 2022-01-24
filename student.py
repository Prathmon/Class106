import csv
import numpy as np

def getDataSource(data_path) :
    marksInPercent = []
    daysPresent = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader :
            marksInPercent.append(float(i["Marks In Percentage"]))
            daysPresent.append(float(i["Days Present"]))
    return{"x" : marksInPercent, "y" : daysPresent}

def findCorelation(datasource) :
    corelation = np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between x and y is :" ,corelation[0,1])

def setup() :
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)

setup()
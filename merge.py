import csv
import pandas as pd

data1=[]
data2=[]
with open("final.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

headers1=data1[0]
planetdata1=data1[1:]

with open("final1.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers2=data2[0]
planetdata2=data2[1:]

headers=headers1+headers2
planetdata=[]
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
    

with open("merged.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

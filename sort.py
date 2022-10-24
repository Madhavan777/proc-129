import csv
import pandas as pd

data=[]
with open("archive_dataset.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
planetdata=data[1:]
for datapoint in planetdata:
    datapoint[2]=datapoint[2].lower()

planetdata.sort(key=lambda planet_data:planet_data[2])
with open("sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open("sorted.csv")as input, open("final1.csv","w",newline="")as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)

        

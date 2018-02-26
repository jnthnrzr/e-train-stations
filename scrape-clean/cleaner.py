"""cleaner.py - Clean data and extract station names to file"""
import csv
import re
import pandas as pd

with open('cleaned-data.csv', 'w') as clean:
    writer = csv.writer(clean)
    with open('scraped-data.csv', 'r') as data:
        reader = csv.reader(data)
        # rownum = 1
        # header = None
        for row in reader:
            # print(len(row))
            if len(row) <= 1:
                continue
            elif 2 < len(row) < 6:
                new_row = [""] + row
                # print(new_row)
                writer.writerow(new_row)
            else:
                # print(row)
                writer.writerow(row)

df = pd.read_csv('cleaned-data.csv')
values = df.Stations
# print(values)
values.to_csv('stations.csv', encoding='utf-8')

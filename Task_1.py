import csv
with open('songs.csv',encoding="utf-8") as f:
    a = list(csv.reader(f,delimiter=";"))
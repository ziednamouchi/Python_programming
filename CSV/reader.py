#CSV: comma separated values
#CSV READER
import csv
#open csv file
with open('my.csv','r+',newline='') as csv_file:
#use csv methode
 reader = csv.reader(csv_file)
 for row in reader:
  print(str(row))

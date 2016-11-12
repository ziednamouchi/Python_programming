#csv writer
import csv
#rows to write
rows = [['1','2', '3'], ['4', '5', '6']]
#open file as csv file
with open('my2.csv', 'w+', newline='') as csv_file:
#methode writer
 writer = csv.writer(csv_file)
 for row in rows:
  writer.writerow(row)


#CSV READER
import csv
#open csv file
with open('my2.csv','r+',newline='') as csv_file:
#use csv methode
 reader = csv.reader(csv_file)
 for row in reader:
  print(str(row))

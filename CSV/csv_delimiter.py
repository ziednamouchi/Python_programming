import csv

#read function
def read(file_location):
 with open(file_location,'r+',newline='') as csv_file:
  reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
  return [row for row in reader]

#write function
def write(file_location,rows):
 with open(file_location,'w+',newline='') as csv_file:
  writer = csv.writer(csv_file,delimiter=' ',quotechar='|')
  for row in rows:
   writer.writerow(row)

#test function
def raw_test():
 columns = int(input("How many columns do you want to write? "))
 input_rows = []
 keep_going = True
 while keep_going:
  input_rows.append([input("column {}: ".format(i + 1)) for i in range(0, columns)])
  ui_keep_going = input("continue? (y/N): ")
  if ui_keep_going != "y":
   keep_going = False

 print(str(input_rows))

 write('raw1.csv', input_rows)
 written_value = read('raw1.csv')
 print(str(written_value))

raw_test()

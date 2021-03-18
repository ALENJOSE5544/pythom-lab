import csv
file=open("C:/Users/student.MCALAB/Desktop/20mca/python/Book1.csv", 'r')
reader = csv.reader(file)
for row in reader:
    print(row)
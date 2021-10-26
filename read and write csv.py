import csv
with open('numbers.csv','r') as a:
    reader=csv.reader(a)

    with open('new_numbers.csv','w') as b:
        writer= csv.writer(b)
        for line in reader:
            writer.writerow(line)

    with open('new_numbers.csv','r') as c:
        reader=csv.DictReader(c)
        for line in reader:
           print(line)

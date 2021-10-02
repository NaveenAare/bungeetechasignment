import csv
file = open("main.csv")
csvreader = csv.reader(file)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

req=[]
for j in range(0,len(rows)):
    temp=[]
    
    temp.append(rows[j][0])
    temp.append(int(rows[j][30]))
    temp.append(int(rows[j][31]))
    
    req.append(temp)


import operator
lis = sorted(req, key=operator.itemgetter(2, 1,0))
lis.reverse()

newheader=['team','yellow cards','red cards']
with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(newheader)
    # write multiple rows
    writer.writerows(lis)
file.close()

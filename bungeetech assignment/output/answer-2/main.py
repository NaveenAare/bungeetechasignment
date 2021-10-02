import csv
file = open("main.csv")
csvreader = csv.reader(file)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

ocupation=[]
ages=[]
maximum=[]
finalmax=[]
finalmin=[]
stri="occupation"
for i in range(0,len(rows)):
    if rows[i][3] in ocupation:
        
        continue
    else:
        ocupation.append(rows[i][3])
ocupation.sort()
for j in ocupation:
    temp=[]
    for i in range(0,len(rows)):
        if j==rows[i][3]:
            temp.append(rows[i][1])
    maximum.append(temp)
for i in range(0,len(maximum)):
    finalmax.append(max(maximum[i]))
    finalmin.append(min(maximum[i]))
ocupation.insert(0,stri)
finalmin.insert(0,"min")
finalmax.insert(0,"max")

l = []
l.append(ocupation)
l.append(finalmin)
l.append(finalmax)
with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    
    # write multiple rows
    writer.writerows(zip(*l))
file.close()

import csv
file = open("main.csv")
csvreader = csv.reader(file)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

newheader=[]
for j in range(0,len(header)):
    if(j!=2):
        newheader.append(header[j])
newrows=[]
myrow=[]
population =0
violent=0
Property=0
Murder=0
Forcible_Rape=0
Robbery=0
Aggravated_assault=0
Burglary=0
Larceny_Theft=0
Vehicle_Theft=0
count=0
year=0
k = len(rows)-len(rows)%10

for i in range(0,int(k/10)):

    if(count==0):
        i=i*10
        for j in range(i,i+10):
             violent=violent+int(rows[j][3])
             Property=Property+int(rows[j][4])
             Murder=Murder+int(rows[j][5])
             Forcible_Rape=Forcible_Rape+int(rows[j][6])
             
             Aggravated_assault=Aggravated_assault+int(rows[j][8])
             Robbery=Robbery+int(rows[j][7])
             Larceny_Theft=Larceny_Theft+int(rows[j][10])
             Burglary=Burglary+int(rows[j][9])
             Vehicle_Theft=Vehicle_Theft+int(rows[j][11])
             population=int(rows[j][1])
             year=rows[i][0]
             
        
        myrow.append(year)
        myrow.append(population)
        myrow.append(violent)
        myrow.append(Property)
        myrow.append(Murder)
        myrow.append(Forcible_Rape)
        myrow.append(Robbery)
        myrow.append(Aggravated_assault)
        myrow.append(Burglary)
        myrow.append(Larceny_Theft)
        myrow.append(Vehicle_Theft)
        newrows.append(myrow)
        myrow=[]
        population =0
        violent=0
        Property=0
        Murder=0
        Forcible_Rape=0
        Robbery=0
        Aggravated_assault=0
        Burglary=0
        Larceny_Theft=0
        Vehicle_Theft=0
        count=0
        year=0

for j in range(k,len(rows)):
    myrow=[]
    violent=violent+int(rows[j][3])
    Property=Property+int(rows[j][4])
    Murder=Murder+int(rows[j][5])
    Forcible_Rape=Forcible_Rape+int(rows[j][6])
    Aggravated_assault=Aggravated_assault+int(rows[j][8])
    Robbery=Robbery+int(rows[j][7])
    Larceny_Theft=Larceny_Theft+int(rows[j][10])
    Burglary=Burglary+int(rows[j][9])
    Vehicle_Theft=Vehicle_Theft+int(rows[j][11])
    population=int(rows[j][1])
    year=rows[k][0]
             
myrow.append(year)
myrow.append(population)
myrow.append(violent)
myrow.append(Property)
myrow.append(Murder)
myrow.append(Forcible_Rape)
myrow.append(Robbery)
myrow.append(Aggravated_assault)
myrow.append(Burglary)
myrow.append(Larceny_Theft)
myrow.append(Vehicle_Theft)
newrows.append(myrow)

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(newheader)

    # write multiple rows
    writer.writerows(newrows)
file.close()
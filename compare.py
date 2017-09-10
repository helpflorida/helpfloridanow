import pandas
import csv
import HTML

ages = []
appends = []
with open("host1.csv", "r") as f:
    r = pandas.read_csv(f)
    ages = list(r["What is the maximum number of people that you can feasibly shelter?"])

with open("help1.csv", "r") as f:
    # Skip the first line
    f.readline()
    for hostline in f:
        if int(hostline.split(",")[6]) in ages:
            print hostline,
            appends.append(hostline)
   
            
this = []
with open("help1.csv", "r") as f:
    r = pandas.read_csv(f)
    this = list(r["How many people (including you) are in your party?"])

with open("host1.csv", "r") as f:
    # Skip the first line
    f.readline()
    for helpline in f:
        if int(helpline.split(",")[7]) in this:
            print helpline, 
            appends.append(helpline)

    
#b = open('output.csv', 'w')
#a = csv.writer(b)
#a.writerows(appends)

htmlcode = HTML.table(appends)
print htmlcode
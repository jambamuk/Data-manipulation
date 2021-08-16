from datetime import datetime
import os
# listen to changes in directory and then use that file and run this when that file appears
entries = []
fileData = []

files = os.listdir('./COLLECTIONS_FNB')
for i in range(len(files)):
    file = open('./COLLECTIONS_FNB/' + files[i], 'r')
    fileData.append(file.read())
    file.close()


def getPremiums(entries):
    premiums = []
    for i in range(len(entries)):
        premiums.append(int(entries[i][1][39:]))
    print(premiums)
    return premiums


def getDate(header):
    dateString = header[7:15]
    date = datetime.strptime(dateString, "%d%m%Y").strftime("%d %B, %Y")
    print(date)


def getFinancialValue(footer):
    financialValue = float(footer[1:].lstrip('0'))/100
    print(f'R {financialValue}')


data = fileData[0].split()
header = data[0]
footer = data[-1]

getDate(header)
data = data[1:-1]

split_points = [i for i, elem in enumerate(data) if 'FNB' in elem]

for i in range(1, len(split_points)):
    entries.append(data[split_points[i-1]:split_points[i]])
entries.append(data[split_points[-1]:])


premiums = getPremiums(entries)
getFinancialValue(footer)
print(f'Total premiums: R {sum(premiums)}')

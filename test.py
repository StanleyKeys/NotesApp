import json




tempList = []

data1 = {'Date': "01.01.01", "Title": "Privet", "Body": "Fuck"}
data2 = {'Date': "12.01.01", "Title": "12", "Body": "2019"}
data3 = {'Date': "31.01.01", "Title": "31", "Body": "2020"}

tempList.append(data1)
tempList.append(data2)
tempList.append(data3)

with open('data.json', 'w') as f:
    json.dump(tempList, f)

print(tempList)
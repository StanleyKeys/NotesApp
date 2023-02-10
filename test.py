from datetime import date
import json

def createjson():





    data1 = []

    with open('db.json', 'w') as file:
        file.write(json.dumps(data1, indent=2, ensure_ascii=False))

# data2 = {'Date': "12.01.01", "Title": "12", "Body": "2019"}
# data3 = {'Date': "31.01.01", "Title": "31", "Body": "2020"}
#
# tempList.append(data1)
# tempList.append(data2)
# tempList.append(data3)

# with open('data.json', 'w') as f:
#     json.dump(tempList, f)

def add_to_json():
    data2 = {'Date': "12.01.01", "Title": "12", "Body": "2019"}
    data = json.load(open("db.json"))
    data.append(data2)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

# add_to_json()
# createjson()
# time = date.today()
# with open('db.json', 'r') as file:
#     data = file.read()
#     json_data = json.loads(data)
#
# print(json_data[0]['Title'])


def createDBlist():
    with open("db.json", "r") as file:
        datb = file.read()
        json_data = json.loads(datb)
    print(json_data)


createDBlist()
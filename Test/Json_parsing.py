import json

fp = r"C:\NNN\Programing\Json\Logglyeventsnew.json"
alldata = json.load(open(fp))
# print(type(alldata))
# for A in alldata:
print(alldata.keys())
print(max(alldata['event']['json']['trace']))

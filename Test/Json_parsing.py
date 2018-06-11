<<<<<<< HEAD
import json

fp = r"C:\NNN\Programing\Json\Logglyeventsnew.json"
alldata = json.load(open(fp))
# print(type(alldata))
# for A in alldata:
print(alldata.keys())
print(max(alldata['event']['json']['trace']))
=======
import json

fp = r"C:\NNN\Programing\Json\Logglyeventsnew.json"
alldata = json.load(open(fp))
# print(type(alldata))
# for A in alldata:
print(alldata.keys())
print(max(alldata['event']['json']['trace']))
>>>>>>> e098262d7bc0c5023aab1e18d9bedf7f221006de

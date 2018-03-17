from urllib.request import urlopen
import re

main = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
# val = 12345 # First Level
val = 25357  # Yes. Divide by two and keep going.
count = 1
# int(count)
# val = 45439


while True:
    res = urlopen(main % val)
    html = res.read().decode('utf-8')
    # print(html)  # to test what is getting printed.
    find = re.search(r"and the next nothing is (\d+)", html)
    if find is None:
        print("Loop Ends", end='\n')
        print(html)
        break
    val = find.group(1)
    print(val)   # This will return a search pattern string.
    print("Loop continues", count, end='\n')
    count = count + 1

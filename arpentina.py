import re
from urllib.request import urlopen


pattern = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

#read text

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = urlopen(url)
data = str(page.read())
 
result = pattern.findall(data)
print(''.join(result))

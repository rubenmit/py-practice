# 
from urllib import urlopen
import re
webpage = urlopen('http://www.python.org')
text = webpage.read()
m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
print m.group(1)

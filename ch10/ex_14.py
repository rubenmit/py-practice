import re

m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print m.group(1) # python
print m.start(1) # 4
print m.end(1) # 10
print m.span(1) # (4, 10)

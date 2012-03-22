import re

text = '"Hm...Err -- are you sure?" he said, sounding insecure.'
pat = r'[.?\-",]+'
print re.findall(pat, text)

pat = '{name}'
text = 'Dear {name}...'
print re.sub(pat, 'Mr. Gumby', text)

print re.escape('www.python.org')

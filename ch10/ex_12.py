import re

some_text = 'alpha, beta....gamma delta'
result = re.split('[, ]+', some_text)
print result

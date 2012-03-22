import re

# greedy
emphasis_pattern = r'\*([^\*]+)\*'
print re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')

# not greedy
emphasis_pattern = r'\*\*(.+?)\*\*' # question mark
re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**!')

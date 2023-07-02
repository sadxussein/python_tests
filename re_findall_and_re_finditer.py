import re

s = list(re.finditer(r"([a-zA-Z][AOEUIaoeui]{2,}[a-zA-Z])", input()))
if any(s):
    print(*list(map(lambda x: x.group()[1:-1], s)), sep='\n')
else:
    print("-1")
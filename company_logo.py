from collections import OrderedDict

s = [*input()]
d = OrderedDict()

for l in s:
    if l in d: d[l] += 1
    else: d[l] = 1

res = sorted(d.items(), key = lambda x: x[1], reverse=True)
for i in range(3):
    print(res[i][0], res[i][1])
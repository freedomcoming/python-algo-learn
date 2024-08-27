import re


target = "0755-890900"

pattern = "(\d{4})-(\d{6})"

res = re.search(pattern, target)


print(res.group())
print(res.group(1))
print(res.group(2))
print(res.groups())

"""
res

0755-890900
0755
890900
('0755', '890900')
"""


import re


target = "0755-890900"

pattern = "(\d{4})-(\d{6})"

res = re.findall(pattern, target)


print(res)

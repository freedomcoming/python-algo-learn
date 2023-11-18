import re


s = '<div class="nam">中国</div>'

res = re.findall(r'<div class="(.*)">(.*?)</div>', s)
print(res)

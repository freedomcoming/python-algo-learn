import requests
from lxml import etree

todicts=requests.get("https://live.nowscore.com/score_print.aspx")

print(todicts.text)

tree_ = etree.HTML(todicts.text)

# print(tree_)

trs = tree_.xpath('/html/body/div[1]/table//tr')
# print(trs)
for tr in trs[:3]:
	hang = [i.xpath('string(.)') for i in tr.xpath('./td')]
	print(hang)

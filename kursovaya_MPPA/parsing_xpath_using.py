from lxml import etree
import requests
import re


session = requests.session()

log = {'email': '89185538008', 'pass': '89185538008veronikA'}
log_url = "https://login.vk.com/?act=login"
session.post(log_url, data=log)
html = session.get('http://vk.com/')

page = html.text

tree = etree.HTML(page)

result = etree.tostring(tree, pretty_print=True, method="html")
print page

'''
for el in tree.find('body').iter('div'):
    if el.attrib.get('class') == 'friends_field':
            print el.text'''


els = tree.xpath('////img[@src][1]/@src')
for i in range(0, len(els)):
    print els[i]
'''
    html = session.get('http://vk.com'+els[i])
    page = html.text
    id = re.findall(ur'<a\s*href="/friends.id=(\d+)', page)

    html = session.get('http://vk.com/friends?id='+(id[0])+'&section=all')
    page = html.text

    tree = etree.HTML(page)
    els = tree.xpath('///div[@class = "friends_field"]/a[@href][1]/@href')
    print els

'''
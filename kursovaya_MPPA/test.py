# -*- coding: utf-8 -*-
import requests
import json
import re
import csv
import os

session = requests.session()

log = {'email': '89185538008', 'pass': '89185538008veronikA'}
log_url = "https://login.vk.com/?act=login"
session.post(log_url, data=log)
html = session.get('http://vk.com/')

page = html.text

js = re.findall(ur'<script\s+.*?src="(.*?)".*?', page)
print js

php = re.findall(ur'<a\s.*?href="(.*?.php)".*?</a>', page)
print php
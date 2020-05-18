import requests
import re

email = ""
password = ""
completed_links = []
input_url = raw_input("Input url: ")
input_deep = raw_input("Input deep: ")
completed_links.append(input_url)
session = requests.session()


def passing_deep(link, how_deep):

    deep = 0

    if link == "http://vk.com/":
        log = {'email': email, 'pass': password}
        log_url = "https://login.vk.com/?act=login"
        res = session.post(log_url, data=log)
    else:
        res = session.get(link)

    print res.url + '\n'
    rt = res.text

    urls = re.findall(ur'<a\s.*?href="(.*?)".*?</a>', rt)
    picture_urls = re.findall(ur'<img\s+.*?src="(.*?)".*?', rt)

    if picture_urls:
        print 'Pictures on this page: ' + str(picture_urls) + '\n'

    if urls:
        print 'Links on this page: ' + str(urls) + '\n'
        for url in urls:
            status = False
            for c_link in completed_links:
                if not url[:7] == 'http://':
                    url = input_url+url
                if url == c_link:
                    status = True
            if status is False and deep < how_deep:
                completed_links.append(url)
                passing_deep(url, int(how_deep)-1)
                deep += 1

    else:
        print "Urls not found\n"

passing_deep(input_url,input_deep)
import requests
import re

email = "nikatina93@yandex.ru"
password = "89185538008veronikA"
completed_links = []
input_url = raw_input("Input url: ")
completed_links.append(input_url)
session = requests.session()


def passing_deep(link, count_passing_links=50):

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
            if status is False and completed_links.__len__() < count_passing_links:
                completed_links.append(url)
                passing_deep(url, count_passing_links)
    else:
        print "Urls not found\n"

passing_deep(input_url)

#<input class="inputText" type="password" name="pass" value="" id="pass" style="width: 152px; margin: 0px">
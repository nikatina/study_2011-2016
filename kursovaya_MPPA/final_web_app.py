# -*- coding: utf-8 -*-
import requests
import re
import json
import csv
import os


input_log_pass = raw_input("Hello! Greetings from VK. Enter your login and password: ")
session = requests.session()
log = {'email': input_log_pass.split()[0], 'pass': input_log_pass.split()[1]}
log_url = "https://login.vk.com/?act=login"
res = session.post(log_url, data=log)


def encode_for_excel(values):
            return [value.encode("utf8") for value in values]


f_out = open('D:\\results.csv', 'wb')
f_out.write(u'\ufeff'.encode('utf8'))
writer = csv.writer(f_out, delimiter=';', lineterminator='\n',
                    quoting=csv.QUOTE_ALL, dialect='excel')


def search_pics_and_links(parameter, output_tp, inp_deep, completed_links, link='http://vk.com/id231013600', count=0):

    count = +1
    res = session.get(link)

    if output_tp == 'screen':
        print res.url + '\n'

    rt = res.text

    if parameter == 'pics':
        picture_urls = re.findall(ur'<img\s+.*?src="(.*?)".*?', rt)
        '''php = re.findall(ur'<a\s.*?href="(.*?.php)".*?</a>', rt)
        js = re.findall(ur'<script\s+.*?src="(.*?)".*?', rt)'''
        if picture_urls:
            if output_tp == 'screen':
                '''print 'Php on this page: ' + str(php) + '\n'
                print 'Js on this page: ' + str(js) + '\n'''''
                print 'Pictures on this page: ' + str(picture_urls) + '\n'
            elif output_tp == 'csv':
                picture_urls[0] = res.url
                writer.writerow(encode_for_excel(picture_urls))
        else:
            if output_tp == 'screen':
                print 'Pictures not found \n'

    if parameter == 'links' or parameter == 'pics':
        urls = re.findall(ur'<a\s.*?href="(.*?)".*?</a>', rt)
        if urls:
            if parameter == 'links':
                if output_tp == 'screen':
                    print 'Links on this page: ' + str(urls) + '\n'
                elif output_tp == 'csv':
                    urls[0] = res.url
                    writer.writerow(encode_for_excel(urls))
            for url in urls:
                status = False
                if not url[:7] == 'http://':
                        url = 'http://vk.com/'+url
                for c_link in completed_links:
                    if url == c_link:
                        status = True
                if status is False and count < int(inp_deep):
                    completed_links.append(url)
                    search_pics_and_links(parameter, output_tp, str(int(inp_deep)-1), completed_links, url, count)


def search_friends(how_deep, output_tp, friends_data_id='231013600', count=0):

    friends_data = {"act": "load_friends_silent",
                    "al": "1",
                    "gid": "0",
                    "id": friends_data_id}

    friends_url = "http://vk.com/al_friends.php"
    login_html = session.post(friends_url, data=friends_data)

    if login_html.text.find(u'Ошибка') == -1:

        start_ind = login_html.text.find('{')
        if friends_data_id == '231013600':
            end_ind = login_html.text.find(',"all_requests"')
        else:
            end_ind = login_html.text.find('}<!><!json>')

        json_data = login_html.text[start_ind + 7: end_ind]
        print json_data

        if json_data:
            json_data = json_data.replace("'", '"')
            if output_tp == 'screen':
                print friends_data_id + '\n' + json_data + '\n'
            js = json.loads(json_data)
            if output_tp == 'csv':
                for ljs in js:
                    writer.writerow(encode_for_excel(ljs))
            count = +1
            if int(how_deep) > count:
                for i in range(0, len(js)):
                    id = js[i][0]
                    search_friends(str(int(how_deep)-1), output_tp, id, count)
            else:
                if output_tp == 'screen':
                    print '\n-----------------------------------------------\n'
                if output_tp == 'csv':
                    writer.writerow(encode_for_excel(['------------------------------------------------------------']))


while True:

    param = raw_input("\nIf you want to get pictures - enter pics \nIf you want to get links - enter links \n"
                      "If you want to get friends - enter frnd\n"
                      "If you want to exit the program - enter exit: ")
    if param == 'pics' or param == 'links' or param == 'frnd':

        if param != 'exit':
            input_deep = raw_input('Enter deep : ')
            try:
                deep = isinstance(int(input_deep), int)
            except Exception:
                deep = False

            if deep:
                output_type = raw_input('Select the type of output - enter screen or csv : ')
                if output_type == 'screen' or output_type == 'csv':

                    if param == 'frnd':
                        search_friends(input_deep, output_type)
                        writer.writerow(encode_for_excel(['\n']))

                    if param == 'links' or param == 'pics':
                        compl_links = []
                        search_pics_and_links(param, output_type, input_deep, compl_links)
                        for i in range(0, 5):
                            writer.writerow(encode_for_excel(['\n']))
                    if output_type == 'csv':
                        os.system("start excel.exe D:\\results.csv")
                else:
                    print 'Wrong type of output'

            else:
                print 'Wrong deep'

    elif param == 'exit':
        print 'See you later, bye!'
        break
    else:
        print 'Wrong param'


f_out.close()

    #89885775141 329832
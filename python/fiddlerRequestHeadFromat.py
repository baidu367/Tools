#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Time : 2021/1/15 14:54
# FileName : fiddlerRequestHeadFromat.py
# Description：fiddler请求头转换成json格式


string = '''
Host: www.*****.com
Connection: keep-alive
Content-Length: 6
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: https://www.*****.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.*****.com/challenge/10
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: 1+1=3

'''
new_sting = ''
headers_dict = {}
data = string.split('\n')
for text in data:
    if text:
        split_text = text.split(':')
        key = split_text[0]
        value = ':'.join(split_text[1:]).strip()
        new_sting += '\t"{}": "{}",\n'.format(key, value)
new_sting = "{%s}" % new_sting

print(new_sting)
'''
{	'Host': 'www.*****.com',
	'Connection': 'keep-alive',
	'Content-Length': '6',
	'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'X-Requested-With': 'XMLHttpRequest',
	'sec-ch-ua-mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
	'sec-ch-ua-platform': '"Windows"',
	'Origin': 'https://www.*****.com',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://www.*****.com/challenge/10',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Cookie': '1+1=3',
}
'''

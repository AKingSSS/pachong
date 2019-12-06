#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
import requests
import json
import pprint
import re
import time

url = 'https://m.weibo.cn/comments/hotflow'

# headers
headers = {
    'Accept': 'application/json, text/plain, */*',
    'MWeibo-Pwa': '1',
    'Referer': 'https://m.weibo.cn/detail/4445543557972385',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': '89690d',
    'cookie': 'T_WM=37488711973; WEIBOCN_FROM=1110006030; ALF=1578121769; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWgi9_wVLPCC_NZMGoxrqED5JpX5KzhUgL.FoMESo-ce0-E1Kq2dJLoI7DWCcLV90.7SoBc; SUB=_2A25w7Mn6DeRhGeRI6VoW-CvJyT6IHXVQLteyrDV6PUJbkdAKLUSlkW1NUx96VldyDA_XoULgTnUNB2Jyy6KvByCJ; SUHB=0YhQa0LGUqNDwe; SCF=AqX_2NHAJff98OZgWLKjoAQUwh5FOfntOgUXkI0iZKQIuqCFf_VDNUKHnoGdycfsAbEnXEf3F13aqmXeniSyEWs.; SSOLoginState=1575532970; MLOGIN=1; XSRF-TOKEN=9be4e0; M_WEIBOCN_PARAMS=oid%3D4445531302904020%26luicode%3D20000061%26lfid%3D4445531302904020%26uicode%3D20000061%26fid%3D4445531302904020'
}
# 下一页额外参数
max_id = ''
# 评论
comment = {}
# 所有评论列表
line = []
# 参数
params = {
    'id': '4445543557972385',
    'mid': '4445543557972385',
    'max_id_type': '0'
}

# 状态
flag = True

while flag:
    if max_id == '':
        # 数据响应
        response = requests.get(url, headers=headers, params=params)
    elif max_id == '0':
        flag = False
        continue
    else:
        params['max_id'] = max_id
        response = requests.get(url, headers=headers, params=params)

    if response.text:
        comment = json.loads(response.text)
    else:
        flag = False
        continue

    if comment['ok'] == 0:
        flag = False
        continue
    max_id = comment["data"]["max_id"]
    for comment_data in comment["data"]["data"]:
        data = comment_data["text"]
        p = re.compile(r'</?\w+[^>]*>')
        data = p.sub(r'', data)
        if len(data) != 0:
            print(data)
            line.append(data)
    time.sleep(1)
else:
    pprint.pprint("len(line) = {}".format(len(line)))
    pprint.pprint(line)

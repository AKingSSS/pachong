import requests
import ascp
import json
import traceback

# 地址
url = 'https://www.toutiao.com/c/user/article/'
# 默认值
max_behot_time = '0'
# 请求头
headers = {
    'accept': 'application/json, text/javascript',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
# cookies
cookies = {"tt_webid": "6719706073617925639"}

try:
    # 循环结束标识
    flag = True
    # 抓取文章标题和地址
    new_list = []
    while flag:
        # 参数
        params = {
            'page_type': '1',
            'user_id': '2299783409577476',
            'max_behot_time': max_behot_time,
            'count': '20',
            'as': ascp.get_as_cp()['as'],
            'cp': ascp.get_as_cp()['cp']
        }
        re = requests.get(url, params=params, headers=headers, cookies=cookies)
        if re.status_code == 200:
            d_initial = json.loads(re.text)
            print("d_initial = {}".format(d_initial))
            # 文章列表信息
            data = d_initial['data']
            # 下一个链接的max_behot_time
            next = d_initial['next']
            if next:
                max_behot_time = next.get('max_behot_time', '')
            else:
                print("下一个链接的max_behot_time不存在！")
                flag = False
            if data:
                for d in data:
                    # 获取文章标题以及文章链接
                    new_d = {}
                    new_d["title"] = d.get("title", "无")
                    new_d["display_url"] = d.get("display_url", "//www.toutiao.com")
                    new_list.append(new_d)
            else:
                print("链接无文章！")
                flag = False
        else:
            print("re.status_code = {}".format(re.status_code))
    else:
        print("new_list = ", json.dumps(new_list).encode("utf-8"))
except Exception:
    print("抛异常！")
    traceback.print_exc()

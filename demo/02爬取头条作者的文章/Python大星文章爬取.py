import requests
import ascp

url = 'https://www.toutiao.com/c/user/article/'
as_ = ascp.get_as_cp()['as']
cp_ = ascp.get_as_cp()['cp']
headers = {
    'accept': 'application/json, text/javascript',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
cookies = {"tt_webid": "6719706073617925639"}
params = {
    'page_type': '1',
    'user_id': '2299783409577476',
    'max_behot_time': '0',
    'count': '20',
    'as': as_,
    'cp': cp_
}
re = requests.get(url, params=params, headers=headers, cookies=cookies)

if re.status_code == 200:
    print(re.text)


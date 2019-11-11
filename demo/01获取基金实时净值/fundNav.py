import requests
from bs4 import BeautifulSoup


# 通过基金代码获取html文档
def getHtml(fundcode):
    url = 'http://fund.eastmoney.com/{}.html?spm=search'.format(fundcode)
    re = requests.get(url)
    return re.content.decode('utf-8')


# 使用bs4解析html文档
def analysisHtml(fundcode):
    # 基金数据
    d = {}
    soup = BeautifulSoup(getHtml(fundcode), 'lxml')
    # 获取基金名称
    d['fundname'] = soup.find(class_='fundDetail-tit').text
    # 获取基金涨幅
    d['fundrate'] = soup.find(id='gz_gszzl').text
    return d

fundcode = '110022'
print(analysisHtml(fundcode))

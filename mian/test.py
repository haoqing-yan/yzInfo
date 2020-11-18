import json
from urllib.parse import urlencode, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

from spider.baseSpider import get_info
from spider.headers import create_headers

if __name__ == '__main__':
    cityUrl = "https://yz.chsi.com.cn/zsml/pages/getSs.jsp"
    subjectUrl = "https://yz.chsi.com.cn/zsml/pages/getMl.jsp"
    url = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"
    queryUrl = "https://yz.chsi.com.cn/zsml/queryAction.do"

    data = get_info(url=subjectUrl)
    files = {'mldm': 'zyxw'}
    print(files)
    for subject in data:
        files['mldm'] = subject['dm']
        response = requests.get(url=url, params=files)
        subjects = json.loads(response.content)
        for one in subjects:
            queryParams = {'xxfs': '', 'yjxkdm': '', 'ssdm': '', 'mldm': '', 'dwmc': '', 'zymc': '', 'pageno' : '1'}
            queryParams['yjxkdm'] = one['dm']
            queryParams['mldm'] = subject['dm']
            queryParams = urlencode(queryParams)
            print(queryParams)
            r = urlparse(queryUrl)
            parts = list(r)
            parts[4] = queryParams
            queryUrl = urlunparse(parts)
            response = requests.get(url=queryUrl, headers=create_headers())
            response.encoding = 'utf-8'
            html = response.text
            print(html)

import json
from urllib.parse import urlencode, urlparse, urlunparse

import requests
import simplejson
from bs4 import BeautifulSoup

from spider.baseSpider import get_info
from spider.headers import create_headers
from util.fileUtil import write

if __name__ == '__main__':
    cityUrl = "https://yz.chsi.com.cn/zsml/pages/getSs.jsp"
    subjectUrl = "https://yz.chsi.com.cn/zsml/pages/getMl.jsp"
    url = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"
    queryUrl = "https://yz.chsi.com.cn/zsml/queryAction.do"

    data = get_info(url=subjectUrl)
    files = {'mldm': 'zyxw'}
    majors = []
    for subject in data:
        # print(subject)
        files['mldm'] = subject['dm']
        response = requests.get(url=url, params=files)
        subjects = json.loads(response.content)
        # print(subjects)
        major = {'majorName': subject['mc'], 'majorCode': subject['dm'], 'singleMajors': subjects}
        # print(major)
        majors.append(major)
        # for one in subjects:
        #     queryParams = {'xxfs': '', 'yjxkdm': '', 'ssdm': '', 'mldm': '', 'dwmc': '', 'zymc': '', 'pageno' : '1'}
        #     queryParams['yjxkdm'] = one['dm']
        #     queryParams['mldm'] = subject['dm']
        #     queryParams = urlencode(queryParams)
        #     print(queryParams)
        #     r = urlparse(queryUrl)
        #     parts = list(r)
        #     parts[4] = queryParams
        #     queryUrl = urlunparse(parts)
        #     response = requests.get(url=queryUrl, headers=create_headers())
        #     response.encoding = 'utf-8'
        #     html = response.text
        #     print(html)
    string = json.dumps(majors).encode('utf-8').decode('unicode_escape')
    write(string)
    print(string)

import json

import requests

from spider.baseSpider import get_info
from util.fileUtil import write
from util.mongodbUtil import insert
from util.mysqlUtil import insert_majors

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
        major = {
            'majorName': subject['mc'],
            'majorCode': subject['dm'],
            'singleMajors': subjects
        }
        # print(insert(major))
        insert_majors(major)
        majors.append(major)

    string = json.dumps(majors).encode('utf-8').decode('unicode_escape')

    write(string)
    print(string)

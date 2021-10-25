import json
import requests

from spider.baseSpider import get_info
from util.mysqlUtil import insert_majors


class YzInfo:

    cityUrl = "https://yz.chsi.com.cn/zsml/pages/getSs.jsp"
    subjectUrl = "https://yz.chsi.com.cn/zsml/pages/getMl.jsp"
    professionalUrl = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"
    queryUrl = "https://yz.chsi.com.cn/zsml/queryAction.do"

    def get_majors(self):

        data = get_info(url=self.subjectUrl)
        files = {'mldm': 'zyxw'}
        majors = []
        for subject in data:
            # print(subject)
            files['mldm'] = subject['dm']
            response = requests.get(url=self.professionalUrl, params=files)
            subjects = json.loads(response.content)
            # print(subjects)
            major = {
                'majorName': subject['mc'],
                'majorCode': subject['dm'],
                'singleMajors': subjects
            }
            # print(insert(major))
            print(insert_majors(major))
            majors.append(major)


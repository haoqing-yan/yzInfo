import re

import requests
from bs4 import BeautifulSoup

from util.mongodbUtil import insert

if __name__ == '__main__':
    mainUrl = 'https://yz.chsi.com.cn'
    queryUrl = "https://yz.chsi.com.cn/zsml/queryAction.do"
    queryParameter = {
        'ssdm': '',
        'dwmc': '',
        'mldm': '08',
        'mlmc': '',
        'yjxkdm': '0812',
        'zymc': '',
        'xxfs': '',
        'pageno': ''
    }
    universities = requests.post(url=queryUrl, params=queryParameter).content
    universities_object = BeautifulSoup(universities, 'lxml')
     # 获取单个大学具体信息
    universities_info = universities_object.findAll('tr')
    university_info = []
     # 该专业招收大学信息
    find_university_page = re.compile(r'<a href="#" onclick="nextPage\(\d+\)">(\d+)</a>')
    university_pageno = universities_object.findAll('a', href="#")
    pageno = []
    for single in university_pageno:
        page_number = re.findall(find_university_page, str(single))
        if len(page_number) == 0:
            continue
        pageno.append(page_number[0])
        # total_pages = pageno[len(pageno) - 1]
    total_pages = pageno[len(pageno) - 1]

    for university in universities_info:
        # 提取具体专业 link
        university_link = re.search(r'\/.*zymc=', str(university.a))
        # 提取招生单位所在地
        find_location = re.compile(r'<td>(.*)</td>')
        # 提取学校名字
        find_name = re.compile(r'<a href="/zsml/querySchAction.do?.*" target="_blank">(.*)</a>')
        location = re.findall(find_location, str(university))
        name = re.findall(find_name, str(university))
        # 跳过表头
        if len(location) == 0:
            continue
        # 访问具体专业 url
        university_faculty_url = mainUrl + str(university_link.group()).replace('amp;', '') + '&pageno='
        # print(university_faculty_url)

        faculty_info_text = requests.get(url=university_faculty_url).content
        # 专业信息页面
        faculty_info = BeautifulSoup(faculty_info_text, 'lxml')
        # 具体专业信息
        faculty_infos = faculty_info.findAll('tr')
        find_pageno = re.compile('<a href="####" onclick="nextPage\(\d+\)">(\d+)</a>')
        faculty_pages = faculty_info.findAll('a', href="####")
        page_list = []
        for page in faculty_pages:
            faculty_page_number = re.findall(find_pageno, str(page))
            if len(faculty_page_number) == 0:
                continue
            page_list.append(faculty_page_number[0])
        print(page_list)

        for item in faculty_infos:
            # 找到具体 id
            find_id = re.compile(r'<a href="/zsml/kskm\.jsp\?id=(.*?)"')
            # 专业信息
            find_info = re.compile(r'<td>(.*)</td>')
            # 入学和教学方式
            find_type = re.compile(r'<td class="ch-table-center">(.*)</td>')
            # 招生人数
            find_number = re.compile(r'document.write\(cutString\(\'(.*?)\',6\)\);', re.S)
            id = re.findall(find_id, str(item))
            # 跳过表头
            if len(id) == 0:
                continue
            items = re.findall(find_info, str(item))
            type = re.findall(find_type, str(item))
            number = re.findall(find_number, str(item))
            university = {
                'id': id[0],
                'name': name[0],
                'location': location[0],
                'faculty': items[0],
                'major': items[1],
                'research': items[2],
                'type': type[1],
                'studentNumber': number[0],
                'comment': number[1]
            }
            # print(insert(university))


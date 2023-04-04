import re
import requests
from bs4 import BeautifulSoup
from util.mongodbUtil import insert


def get_page_numbers(anchors, regex):
    page_numbers = []
    for anchor in anchors:
        number = re.findall(regex, str(anchor))
        if number:
            page_numbers.append(number[0])
    return page_numbers


def process_universities(universities_object):
    find_university_page = re.compile(r'<a href="#" onclick="nextPage\(\d+\)">(\d+)</a>')
    university_pageno = universities_object.findAll('a', href="#")
    return get_page_numbers(university_pageno, find_university_page)


def process_faculties(faculty_info):
    find_pageno = re.compile('<a href="####" onclick="nextPage\(\d+\)">(\d+)</a>')
    faculty_pages = faculty_info.findAll('a', href="####")
    return get_page_numbers(faculty_pages, find_pageno)


def extract_university_data(universities_info):
    mainUrl = 'https://yz.chsi.com.cn'
    university_data = []
    for university in universities_info:
        university_link = re.search(r'\/.*zymc=', str(university.a))
        location = re.findall(r'<td>(.*)</td>', str(university))
        name = re.findall(r'<a href="/zsml/querySchAction.do?.*" target="_blank">(.*)</a>', str(university))

        if not location:
            continue

        university_data.append({
            'link': mainUrl + str(university_link.group()).replace('amp;', '') + '&pageno=',
            'name': name[0],
            'location': location[0]
        })
    return university_data


def main():
    queryUrl = "https://yz.chsi.com.cn/zsml/queryAction.do"
    queryParameter = {
        'ssdm': '',
        'dwmc': '',
        'mldm': '08',
        'mlmc': '',
        'yjxkdm': '0812',
        'zymc': '',
        'xxfs': '',
        'pageno': '2'
    }
    universities = requests.post(url=queryUrl, params=queryParameter).content
    universities_object = BeautifulSoup(universities, 'lxml')

    universities_info = universities_object.findAll('tr')
    university_data = extract_university_data(universities_info)

    total_pages = process_universities(universities_object)

    for university in university_data:
        university_faculty_url = university['link']
        faculty_info_text = requests.get(url=university_faculty_url).content
        faculty_info = BeautifulSoup(faculty_info_text, 'lxml')
        faculty_infos = faculty_info.findAll('tr')

        faculty_pages = process_faculties(faculty_info)

        for item in faculty_infos:
            id = re.findall(r'<a href="/zsml/kskm\.jsp\?id=(.*?)"', str(item))
            if not id:
                continue

            items = re.findall(r'<td>(.*)</td>', str(item))
            type = re.findall(r'<td class="ch-table-center">(.*)</td>', str(item))
            number = re.findall(r'document.write\(cutString\(\'(.*?)\',6\)\);', str(item), re.S)

            university_record = {
                'id': id[0],
                'name': university['name'],
                'location': university['location'],
                'faculty': items[0],
                'major': items[1],
                'research': items[2],
                'type': type[1],
                'studentNumber': number[0],
                'comment': number[1]
            }
            # print(university_record)
            print(insert(university_record))

if __name__ == '__main__':
    main()

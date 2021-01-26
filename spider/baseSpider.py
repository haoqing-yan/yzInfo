# 此代码仅供学习与交流，请勿用于商业用途。
# 爬虫基类
# 爬虫名常量，用来设置爬取哪个站点
import json
import random
from datetime import time

import requests

from spider.headers import create_headers

thread_pool_size = 50
# 具体时间可以修改random_delay()，由于多线程，建议数值大于10
RANDOM_DELAY = False


class BaseSpider(object):
    @staticmethod
    def random_delay():
        if RANDOM_DELAY:
            time.sleep(random.randint(0, 16))


def get_info(url):

    if url.find("www") == -1:
        headers = create_headers()
        response_info = requests.get(url=url, headers=headers)
        html = response_info.content
        data = json.loads(html)
    return data

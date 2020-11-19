import os
import time


def write(context):
    now = time.strftime("%Y%m%d", time.gmtime())
    if os.path.exists('../data') is False:
        os.mkdir('../data')
    fileName = '../data/' + now + '.json'
    file = open(fileName, 'w+', encoding='utf-8')
    file.write(context)


if __name__ == '__main__':
    write("")

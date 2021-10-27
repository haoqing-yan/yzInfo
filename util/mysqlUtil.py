import json
import re
import time

import jsonify as jsonify
import pymysql
import requests


def insert_majors(data):
    db = pymysql.connect(host='127.0.0.1', user='root', password='WULIkanwuli9', db='yzinfo')
    cursor = db.cursor()
    now = time.strftime('%Y%m%d', time.localtime(time.time()))
    for subject in data['singleMajors']:
        sql = 'INSERT INTO majors(majors, majorCode, subjectMajor, subjectMajorCode, createTime) VALUES(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' \
              % (data['majorName'], data['majorCode'], subject['mc'], subject['dm'], now)
        try:
            result = cursor.execute(sql)
            db.commit()
        except:
            result = 0
            db.rollback()
    return result


def query_majors():
    db = pymysql.connect(host='127.0.0.1', user='root', password='WULIkanwuli9', db='yzinfo',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "SELECT majors,majorCode,subjectMajor,subjectMajorCode FROM majors"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
    except:
        # result = 0
        db.rollback()
    return result


def insert_universities(data):
    db = pymysql.connect(host='127.0.0.1', user='root', password='WULIkanwuli9', db='yzinfo',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    now = time.strftime('%Y%m%d', time.localtime(time.time()))
    sql = 'INSERT INTO universities(id, name, location, faculty, major, research, type, studentNumber, comment, createTime) VALUES (' \
          '\'%s\' ,\'%s\' ,\'%s\' ,\'%s\' ,\'%s\' ,\'%s\' ,\'%s\' ,\'%s\',\'%s\' ,\'%s\' )' \
          % (data['id'], data['name'], data['location'],
             data['faculty'], data['major'], data['research'],
             data['type'], data['studentNumber'], data['comment'], now)
    # print(sql)
    try:
        result = cursor.execute(sql)
        db.commit()
    except:
        result = 0
        db.rollback()
    return result

if __name__ == '__main__':
    all_majors = query_majors()
    print(all_majors[0])



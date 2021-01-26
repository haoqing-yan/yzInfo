import pymysql

def insert_majors(data):
    db = pymysql.connect("127.0.0.1", "root", "WULIkanwuli9", "yzinfo")
    cursor = db.cursor()
    for subject in data['singleMajors']:
        sql = "INSERT INTO majors(majors, majorCode, subjectMajor, subjectMajorCode) VALUES(\'%s\', \'%s\', \'%s\', \'%s\')" \
              % (data['majorName'], data['majorCode'], subject['mc'], subject['dm'])
        try:
            result = cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    return result
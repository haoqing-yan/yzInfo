import time
import pymysql.cursors
import yaml

# 读取 YAML 配置文件
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=config['database']['host'],
            user=config['database']['user'],
            password=config['database']['password'],
            db=config['database']['db'],
            cursorclass=pymysql.cursors.DictCursor,
            charset=config['database']['charset']
        )

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# 处理 major_categories 表的插入
def insert_major_categories(major_code, majors):
    with Database() as db:
        cursor = db.cursor()
        now = time.strftime(config['other']['date_format'], time.localtime())
        sql = "INSERT INTO major_categories(majorCode, majors) VALUES(%s, %s)"
        try:
            result = cursor.execute(sql, (major_code, majors))
            db.commit()
            return result
        except Exception as e:
            print(f"Failed to insert major category: {e}")
            db.rollback()
            return 0


# 处理 majors 表的插入
def insert_majors(major_code, subject_major_code, subject_major):
    with Database() as db:
        cursor = db.cursor()
        now = time.strftime(config['other']['date_format'], time.localtime())
        sql = "INSERT INTO majors(majorCode, subjectMajorCode, subjectMajor, createTime) VALUES(%s, %s, %s, %s)"
        try:
            result = cursor.execute(sql, (major_code, subject_major_code, subject_major, now))
            db.commit()
            return result
        except Exception as e:
            print(f"Failed to insert major: {e}")
            db.rollback()
            return 0


# 处理 universities 表的插入
def insert_universities(id, name, location, faculty, major, research, type, student_number, comment):
    with Database() as db:
        cursor = db.cursor()
        now = time.strftime(config['other']['date_format'], time.localtime())
        sql = "INSERT INTO universities(id, name, location, faculty, major, research, type, studentNumber, comment, createTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            result = cursor.execute(sql,
                                    (id, name, location, faculty, major, research, type, student_number, comment, now))
            db.commit()
            return result
        except Exception as e:
            print(f"Failed to insert university: {e}")
            db.rollback()
            return 0


# 处理 exam 表的插入
def insert_exam(id, name, politics, foreign_language, professional_subject1, professional_subject2):
    with Database() as db:
        cursor = db.cursor()
        now = time.strftime(config['other']['date_format'], time.localtime())
        sql = "INSERT INTO exam(id, name, politics, foreignLanguage, professionalSubject1, professionalSubject2, createTime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            result = cursor.execute(sql, (
                id, name, politics, foreign_language, professional_subject1, professional_subject2, now))
            db.commit()
            return result
        except Exception as e:
            print(f"Failed to insert exam: {e}")
            db.rollback()
            return 0


def query_majors():
    with Database() as db:
        cursor = db.cursor()
        sql = "SELECT majorCode, subjectMajorCode, subjectMajor, createTime, updateTime FROM majors"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            db.commit()  # 这里通常不需要commit，因为查询操作不涉及数据变更
            return results
        except Exception as e:
            print(f"Failed to query majors: {e}")
            db.rollback()  # 查询失败通常不需要rollback，但保留以应对潜在的触发器等复杂情况
            return []


if __name__ == '__main__':
    # 示例调用：查询 majors 表中的所有数据
    all_majors = query_majors()
    print(all_majors if all_majors else 'No majors found.')

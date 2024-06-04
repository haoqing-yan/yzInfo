import pymongo

class MongoDatabase:
    def __init__(self, db_name, collection_name, host='localhost', port=27017):
        self.client = pymongo.MongoClient(f'mongodb://{host}:{port}/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data):
        """插入数据，如果数据已存在则不插入"""
        if self.collection.find_one(data) is None:
            return self.collection.insert_one(data)
        return 'DB had record'

    def get_all(self):
        """获取集合中所有文档"""
        return list(self.collection.find())

    def close(self):
        """关闭数据库连接"""
        self.client.close()

# 使用示例
if __name__ == '__main__':
    db = MongoDatabase('zyInfo', 'majors')
    # 插入数据示例
    data = {'majorName': 'Computer Science', 'majorCode': 'CS101'}
    print(db.insert(data))  # 插入数据

    # 获取所有专业数据
    majors = db.get_all()
    for major in majors:
        print(major)

    # 完成操作后关闭数据库连接
    db.close()

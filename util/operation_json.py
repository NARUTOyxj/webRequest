import json

class OperationJson:

    def __init__(self):
        self.data = self.read_data()

    # 打开json文件
    def read_data(self):
        with open('./dataconfig/login.json') as fp:
            data = json.load(fp)
            return data

    #读取json数据
    def get_data(self,id):
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('login_normal'))
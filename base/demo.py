import requests
import json

class RunMain:
    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        # return json.dumps(res,indent=2,sort_keys=True).json() # 格式化json
        return res

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return res

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

# if __name__ == '__main__':
#     url = 'http://scmpcapp.loongjoy.com/#/user/login#zh'
#     data = {
#         'nickname':'plat_yxj',
#         'password':'123456'
#     }
#     run = RunMain(url,'POST',data)
#     pint(run.res)
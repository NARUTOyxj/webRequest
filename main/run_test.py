import sys
sys.path.append('D:/project/webRequest')
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    #程序执行主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    #获取依赖的响应数据
                    depend_reponse_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_reponse_data
                res = self.run_method.run_main(method,url,request_data,header) 

                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)
        print(len(pass_count))
        print(len(fail_count))

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

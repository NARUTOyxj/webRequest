import unittest
import json
import HTMLTestRunner
import mock
from demo import RunMain
from mock_demo import mock_test

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
    
    def test_01(self):  #测试用例的名称以test开头
        url  = 'http://scmbase.loongjoy.com/api/auth/postToken'
        data = {
            'fromSys': 'scmpcapp',
            'lang': 'zh',
            'nickname':'plat_yxj',
            'password': '123456'
        }
        res = self.run.run_main(url,'POST',data)
        # print(res) #返回结果
        #添加断言，如果失败返回message
        self.assertEqual(res['status'],0,'测试失败')
        print('测试用例01')

    # @unittest.skip('test_02')  #跳过测试用例
    def test_02(self):
            url  = 'http://scmbase.loongjoy.com/api/auth/postToken'
            data = {
                'fromSys': 'scmpcapp',
                'lang': 'zh',
                'nickname':'plat06',
                'password': '123456'
            }
            res = self.run.run_main(url,'POST',data)
            # print(res) #返回结果
            #添加断言，如果失败返回message
            self.assertEqual(res['status'],0,'测试失败')
            print('测试用例02')

    #mock 练习
    def test_03(self):
            url  = 'http://scmbase.loongjoy.com/api/auth/postToken'
            data = {
                'fromSys': 'scmpcapp',
                'lang': 'zh',
                'nickname':'plat06',
                'password': '123456'
            }
            """
            #mock未封装时的方法
            mock_data = mock.Mock(return_value= data)
            self.run.run_main = mock_data
            res = self.run.run_main(url,'POST',data)
            """
            #mock封装后的方法
            res = mock_test(self.run.run_main,data,url,'POST',data)

            print(res) #返回结果
            #添加断言，如果失败返回message
            self.assertEqual(res['lang'],'zh','测试失败')
            print('测试用例03')
if __name__ == '__main__':
    #定义报告存放路径
    fp = open('./report/htmlreport.html','wb')    
    # unittest.main()
    suite = unittest.TestSuite()  #定义一个测试集
    suite.addTest(TestMethod('test_01'))  #往测试集加测试用例
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = 'test report')
    runner.run(suite)
    fp.close()
    # unittest.TextTestRunner().run(suite) #运行测试集，测试用例的执行顺序为测试用例的名称升序

    


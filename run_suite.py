# 导包
import os
import time
import unittest

# from tools import HTMLTestRunner
import HTMLTestRunner_PY3
# 实例化测试套件
from script.test_ihrm_login import TestIHRMLogin

suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 设置测试报告的路径和名称
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm.html"
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理 系统接口测试报告",
                                           description="测试登陆接口和员工管理模块")
    # 使用Runner运行测试套件生成测试报告
    runner.run(suite)
    print("构建后")
    print("!"*50)
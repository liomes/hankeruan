from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread
class successT(Thread):
    def run(self):
        test = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestSuccess.py")

        runner = HTMLTestRunner.HTMLTestRunner(
            title="成功测试报告",
            description="详细测试报告",
            verbosity=1,
            stream=open(file="成功测试报告.html", mode="w+", encoding="utf-8")
        )
        runner.run(test)
class failT(Thread):
    def run(self):
        test = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Testfail.py")

        runner = HTMLTestRunner.HTMLTestRunner(
            title="失败测试报告",
            description="详细测试报告",
            verbosity=1,
            stream=open(file="失败测试报告.html", mode="w+", encoding="utf-8")
        )
        runner.run(test)
success = successT()
fail = failT()

success.start()
fail.start()
from selenium import webdriver
from unittest import TestCase
from StartData import StartData
from StartOpen import StartOper
from ddt import ddt, data


@ddt
class TestLogin(TestCase):
    @data(*StartData.No_data)
    def testLogin_No(self, testData):
        user = testData["user"]
        pws = testData["pws"]
        exp = testData["expect"]

        # 执行
        driver = webdriver.Chrome()
        login1 = StartOper(driver)
        login1.login(user, pws)

        # 实际结果
        r = login1.getError_result()
        driver.quit()
        # 断言
        self.assertEqual(r, exp)
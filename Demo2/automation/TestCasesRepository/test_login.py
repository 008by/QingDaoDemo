import unittest
from automation.WebPages.test_login_page import LoginPage
from automation.WebPages.Base import Base
from automation.CommonLibrary.TestCaseInfo import TestCaseInfo
import automation.CommonLibrary.LogUtility as Log
import automation.CommonLibrary.Common as cc
import time
from selenium import webdriver



class Test_TC_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1, name="testLogin", owner='lhz')
        Log.CreateLoggerFile("login_movie")


    def test_login(self):

        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            Log.Log("Open Base site" + self.base_url)
            loginPage = LoginPage(self.driver,self.base_url)
            loginPage.open(self.base_url)
            loginPage.login_action("admin","admin")
            self.testCaseInfo.result = "Pass"
            self.assertIn("退出", self.driver.page_source)

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            Log.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)


    def tearDown(self):
        self.driver.close()



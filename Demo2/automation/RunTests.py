import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib,os
import automation.CommonLibrary.LogUtility as LogUtility
import automation.CommonLibrary.EmailUtils as EmailUtils


class RunTests(object):

    def LoadAndRunTestCases(self):
        try:
            test_dir = 'D:\\pythonCode\\Demo2\\automation\\TestCasesRepository'
            test_report = 'D:\\pythonCode\\Demo2\\report'
            discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

            now_time = time.strftime("%Y%m%d%H%M%S")
            file_name = test_report + '\\' + now_time + 'result.html'
            fp = open(file_name, 'wb')
            runner = HTMLTestRunner(stream=fp, title="MyMovie测试报告", description="运行环境： firefox")

            runner.run(discover)
            fp.close()


        except Exception as err:
            LogUtility.logger.debug("Failed running test cases, error message: {}".format(str(err)))
        finally:
            EmailUtils.send_report()




if __name__ == "__main__":
    newrun = RunTests()
    newrun.LoadAndRunTestCases()
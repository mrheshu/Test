#coding:utf-8
import unittest
import os
from selenium import webdriver
from time import sleep
import HTMLTestRunner
import time

class Dttest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start setup')
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.2'
        desired_caps['deviceName'] = 'iPhone 4s'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDown')

    def test_test(self):
        sleep(5)
        print('test passed')
    
    #text测试
    def test_m(cls):
        cls.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]").click()
        sleep(5)
        print('test_m passed')

# wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]").click()

    def test_A(cls):
        cls.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[2]").click()
        sleep(5)
        print('test_A passed')

    def test_B(self):
        i = 10/0
        print('test_B passed')

    def test_C(cls):
        cls.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(5)
        print('test_C passed')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dttest('test_test'))
  #  suite.addTest(Dttest('test_m'))
    suite.addTest(Dttest('test_A'))
   # suite.addTest(Dttest('test_B'))
    suite.addTest(Dttest('test_C'))
    unittest.TextTestRunner(verbosity=2).run(suite)

    timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    filename = '/Users/heshuwei1/Desktop/python/report/'+timestr+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()

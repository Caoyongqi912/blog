import os
import time
import unittest

from django.http import HttpResponse
from selenium import webdriver

from Pro_Web.models import WebCaseStep, WebCase

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# C:\Users\fanhonglian\Desktop\Django_blog\Pro_Web


def getid(request, aid):
    if request.method == 'GET':
        web = WebCase.objects.get(pk=aid)
        url = web.we
        Search(aid)


class Search(unittest.TestCase):
    def __init__(self, wid,url):
        super(Search, self).__init__()
        self.wid = wid
        self.url = url

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(1)

    def test_readsql(self):
        web_case = WebCase.objects.get(pk=self.wid)
        web_case_step = WebCaseStep.objects.filter(web_case=web_case)
        # <QuerySet [<WebCaseStep: web_网站测试_demo_title_1>, <WebCaseStep: web_网站测试_demo_titile_2>]>
        for i in web_case_step:
            self.web_test(i)

    def web_test(self, case_list):
        for i in case_list:
            try:
                case_id = i.id
                find_method = i.web_find_method
                evelement = i.web_element
                opt_method = i.web_opt_method
                test_data = i.web_test_data
            except Exception as e:
                return '用例格式錯誤 %s' % e
            time.sleep(2)
            if opt_method == 'sendkeys' and find_method == 'find_element_by_id':
                self.driver.find_element_by_id(evelement).send_keys(test_data)
            elif opt_method == 'click' and find_method == 'find_element_by_name':
                self.driver.find_element_by_name(evelement).click()
            elif opt_method == 'click' and   find_method == 'find_element_by_id':
                self.driver.find_element_by_id(evelement).click()

    def tearDown(self):
        self.driver.quit()




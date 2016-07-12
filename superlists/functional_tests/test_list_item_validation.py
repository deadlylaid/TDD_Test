from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

from .base import FunctionalTest

import sys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        #에디스는 메인 페이지에 접속해서 빈 아이템을 실수로 등록하려고 한다
        # 입력상자가 비어있는 상태에서 엔터키를 누른다
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #페이지가 새로고침 되고, 빈아이템을 등록할 수 없다는
        #메시지가 표시된다.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "빈 아이템은 등록할 수 없다.")

        #다른 아이템을 입력하면 정상처리된다
        self.browser.find_element_by_id('id_new_item').send_keys('1: 우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

        #고의로 다시한번 빈 아이템을 등록한다
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #리스트 페이지에 에러메시지가 표시된다.
        self.check_for_row_in_list_table('1: 우유 사기')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "빈 아이템을 등록할 수 없습니다")

        #아이템을 입력하면 정상작동한다.
        self.browser.find_element_by_id('id_new_item').send_keys('tea 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: tea 만들기')


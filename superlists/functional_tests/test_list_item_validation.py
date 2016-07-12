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

        #페이지가 새로고침 되고, 빈아이템을 등록할 수 없다는
        #메시지가 표시된다.

        #다른 아이템을 입력하면 정상처리된다

        #고의로 다시한번 빈 아이템을 등록한다

        #리스트 페이지에 에러메시지가 표시된다.

        #아이템을 입력하면 정상작동한다.

        self.fail('wirte me!')

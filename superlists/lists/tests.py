from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.templates.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)

#strip() 은 텍스트 편집기에 따라 파일 마지막에 라인(\n)이 강제로 추가되는 것을 방지하기 위해 쓴다
        self.assertTrue(response.content.strip().endswith(b'</html>'))
# Create your tests here.

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request=request)
        self.assertEqual(response.content.decode(), expected_html)
        self.assertIn(b'<title>To-Do lists</title>', response.content)
    
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
                'home.html',
                {'new_item_text': '신규 작업 아이템'},
                request=request,
                )
        self.assertEqual(response.content.decode(), expected_html)


#strip() 은 텍스트 편집기에 따라 파일 마지막에 라인(\n)이 강제로 추가되는 것을 방지하기 위해 쓴다
#        self.assertTrue(response.content.strip().endswith(b'</html>'))
# Create your tests here.

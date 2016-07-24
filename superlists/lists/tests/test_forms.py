from django.test import TestCase

from lists.forms import ItemForm


class ItemFormTest(TestCase):

    def test_case_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="작업 아이템 입력"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())


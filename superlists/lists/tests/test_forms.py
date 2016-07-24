from django.test import TestCase

from lists.forms import ItemForm, EMPTY_LIST_ERROR


class ItemFormTest(TestCase):

    def test_case_renders_item_text_input(self):
        form = ItemForm(data={'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
                form.errors['text'],
                [EMPTY_LIST_ERROR]
                )
#        self.assertIn('placeholder="작업 아이템 입력"', form.as_p())
#        self.assertIn('class="form-control input-lg"', form.as_p())
#

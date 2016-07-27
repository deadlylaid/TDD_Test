from django.test import TestCase

from lists.forms import ItemForm, EMPTY_LIST_ERROR
from lists.models import Item, List


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

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text':'do me'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)
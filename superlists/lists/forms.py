from django import forms

from lists.models import Item

EMPTY_LIST_ERROR = "You Can't Have An Empty List Item"

class ItemForm(forms.models.ModelForm):



    class Meta:

        model = Item
        fields = ('text',)
        widgets = {
                'text': forms.fields.TextInput(
                    attrs={
                        'placeholder': '작업 아이템 입력',
                        'class': 'form-control input-lg',
                        }
                    ),
                }
        error_messages = {
                'text': {'required': EMPTY_LIST_ERROR}
                }

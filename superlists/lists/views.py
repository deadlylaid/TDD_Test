from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from lists.models import Item, List
from lists.forms import ItemForm

# Create your views here.
def home_page(request): 

    return render(
            request,
            'home.html',
            {'form': ItemForm()},
            )

def view_list(request, list_id):

    list_ = List.objects.get(id=list_id)
    error = None
#    items = Item.objects.filter(list=list_)

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You Can't Have An Empty List Item"

    return render(
            request,
            'list.html',
            {'list':list_,
            'error': error}
            )

def new_list(request):
    list_ = List.objects.create()
    
    item = Item.objects.create(text=request.POST['text'], list=list_)

    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You Can't Have An Empty List Item"
        return render(request, 'home.html',{"error":error})
                
    return redirect(
            list_
            )


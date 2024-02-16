from django.shortcuts import render, redirect
from Categories.forms import categoryForm
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        cat_form = categoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('show_task')
    else:
        cat_form = categoryForm()
    return render(request,'add_categories.html', {'form': cat_form})
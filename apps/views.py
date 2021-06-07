from django.shortcuts import render, redirect
from .models import Data
from django.contrib import messages
from .forms import DataForm


# Create your views here.
def index(request):
    if request.method == "GET":
        name = request.GET.get('name', '')
        age = request.GET.get('age', '')
        num = request.GET.get('num', '')
        mail = request.GET.get('mail', '')
        data = Data(name=name, age=age, num=num, mail=mail)
        data.save()
        messages.success(request, 'You are successfully Signed In...')
    return render(request, 'index.html')


def dash(request):
    data = Data.objects.all()
    params = {'data': data}
    return render(request, 'dash.html', params)


def destroy(request, id):
    item = Data.objects.get(id=id)
    item.delete()
    return redirect("/dash")


def edit(request, id):
    item = Data.objects.get(id=id)
    return render(request, 'edit.html', {'item': item})


def update(request, id):
    item = Data.objects.get(id=id)
    form = DataForm(instance=item)
    if request.method == 'GET':
        form = DataForm(request.GET, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/dash")
    return render(request, 'edit.html', {'item': item})

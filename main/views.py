from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.


def index(request):
    tasks = Task.objects.order_by('-id')  # сортировка от новых к старым all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':  # обработка нажатия кнопки (внесение изменений в бд)
        form = TaskForm(request.POST)
        if form.is_valid():  # проверка корректности ввода
            form.save()
            return redirect('home')  # переадресация на страницу
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

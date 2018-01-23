from django.shortcuts import render, HttpResponse, redirect
from models import User
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users/index.html', context)

def user(request, id):
    id = User.objects.get(id=id)
    context = {
        'current_user': id
    }
    return render(request, 'users/user.html', context)

def create(request):
    return render(request, 'users/create.html')

def add(request):
    user = User.objects.create(first_name=request.POST.get('first_name', False), last_name=request.POST.get('last_name', False), email=request.POST.get('email', False))
    return redirect('/')

def edit(request, id):
    id = User.objects.get(id=id)
    context = {
        'current_user': id
    }
    return render(request, 'users/update.html', context)

def update(request, id):
    id = User.objects.get(id=id)
    id.first_name = request.POST.get('first_name')
    id.last_name = request.POST.get('last_name')
    id.email = request.POST.get('email')
    id.save()
    return redirect('/')

def delete(request, id):
    id = User.objects.get(id=id)
    id.delete()
    return redirect('/')
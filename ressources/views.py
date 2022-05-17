
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Category, Salary
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required
def home(request):
    return render(request, 'registration/success.html', {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
    
def index(request):
    salarys = Salary.objects.all()
    context = {'salarys': salarys}
    return render(request, 'templates/salary/index.html', context)
    
def create(request):
    salary = Salary(amount=request.POST['amount'], date=request.POST['date'] , user_id= request.user.id)
    salary.save()
    return redirect('salary.index')
 
def edit(request, id):
    salary =Salary.objects.get(id=id)
    context = {'salary': salary}
    return render(request, 'templates/salary/edit.html', context)
 
def update(request, id):
    salary = Salary.objects.get(id=id)
    salary.amount = request.POST['amount']
    salary.date = request.POST['date']
    salary.save()
    return redirect('salary.index')
 
def delete(request, id):
    salary = Salary.objects.get(id=id)
    salary.delete()
    return redirect('salary.index')

def index_categ(request):
    categorys = Category.objects.all()
    context = {'categorys' : categorys}

    return render(request, 'templates/category/index.html', context)

def create_categ(request):
    category = Category(max_amout=request.POST['max'], label=request.POST['name'] , user_id= request.user.id)
    category.save()
    return redirect('category.index')    

def edit_categ(request, id):
    category =Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'templates/category/edit.html', context)

def update_categ(request, id):
    category = Category.objects.get(id=id)
    category.max_amout = request.POST['max']
    category.label = request.POST['name']
    category.save()
    return redirect('category.index')
    
def delete_categ(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category.index')
    

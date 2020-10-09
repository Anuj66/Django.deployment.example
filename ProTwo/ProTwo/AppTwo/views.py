from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUser
# Create your views here.

def index(request) :
    return render(request, 'AppTwo/index.html')

def help(request) :
    data = {'insert_me':"Hello i am from views.py"}
    return render(request,'AppTwo/index.html',context = data)

def user(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")
    
    return render(request, 'AppTwo/users.html',{'form': form})
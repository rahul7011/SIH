from django.shortcuts import render,redirect                    #added redirect support
from django.contrib.auth.models import auth                 #added support for user and auth
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # check = auth.authenticate(username=username,password=password)
        check = auth.authenticate(email=email,password=password)

        if check is not None:
             auth.login(request,check)
             return redirect('/')
        else:
            messages.info(request,'Invalid credentials!')
            # raise ValueError('Users must have an email address')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':                    #if method is post then answer this
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!')
            return redirect('accounts:register')   
        elif password is not None and password != password_2:
            messages.info(request,"Password doesn't matched!")
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(name=name,email=email,password=password)
            user.save();          #above firstname is from main database and after equal is our given name
        return redirect('accounts:login')
    else:
        return render(request,'signup.html')    
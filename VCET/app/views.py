from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(username)
        print(password)
        
        user = authenticate(username=username, password=password)
        
        context = {
            'user' : username,
        }
        
        request.session['login_context'] = context
        
        print('before if')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {'error_invalid':True})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        errors = {}
        
        print(username)
        print(password)
        
        if User.objects.filter(username=username).exists():
            errors['existing_user'] = True
        if cpassword != password:
            errors['errors_password'] = True
        try:
            validate_password(password)
        except ValidationError as error:
            errors['error_pass_validation'] = error
            
        if errors:
            errors.update({'error': True, 'username': username, 'password': password})
            return render(request, "signup.html", errors)
        else:
            myuser = User.objects.create_user(username=username, password=password)
            myuser.save()
            return render(request, "login.html",)
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return render(request, "login.html")
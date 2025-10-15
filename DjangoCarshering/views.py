from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def index(request):
    return render(request, 'DjangoCarshering/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('main_page')
    return render(request, 'DjangoCarshering/login.html')

def logout_view(request):
   pass

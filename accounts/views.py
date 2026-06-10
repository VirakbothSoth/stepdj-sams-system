from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .utils import generate_token

# Create your views here.
def login_view(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            token = generate_token(user)
            res = redirect('dashboard')
            res.set_cookie(
                'jwt',
                token,
                httponly=True
            )
            return res
        else:
            return render(req, 'accounts/login.html', {'error': 'Invalid credits'})
    return render(req, 'accounts/login.html')

def logout_view(req):
    res = redirect('login')
    res.delete_cookie('jwt')
    return res
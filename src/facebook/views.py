from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import RegisterForm, LoginForm


User = get_user_model()

def home_page(request):
	context = {
		"home_page": "Selamat Datang"
	}
	return render(request, 'base/home.html', context)


def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form' : form,
		'title' : 'Register Form'
	}
	if form.is_valid():
		username = form.cleaned_data.get("username")
		email    = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
	return render (request, 'auth/register.html', context)


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form,
		'title': 'Login Form',
	}
	print(request.user.is_authenticated())
	if form.is_valid():
		
		context = {'form': LoginForm()}
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user 	 = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return redirect('/register')
	return render(request, 'auth/login.html', context)
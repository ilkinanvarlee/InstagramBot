from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout
from instagram.forms import InstagramForm
from django.contrib.auth.forms import AuthenticationForm
from instagram.models import Instagram
from django.contrib.auth.decorators import login_required


def index(request):
	print(1234567890, request.user)
	return render(request=request, template_name="index.html")


def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("user:instagram")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			messages.info(request, 'login was ela')
			return redirect("user:dashboard")
		else:
			messages.error(request, 'form is incorrect')
	return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("user:index")


def instagram(request):
	if request.method == 'POST':
		form = InstagramForm(request.POST)
		if form.is_valid():
			form.instance.user = request.user
			form.save()
			messages.success(request, "Your username and password saved check your dashboard periodically .")
			return redirect("user:dashboard")
		messages.error(request, "Invalid information, try again .")
	form = InstagramForm()
	return render(request=request, template_name="instagram.html", context={"instagram_form": form})


# @login_required
def dashboard(request):
	datas = Instagram.objects.get(user=request.user)
	context = {'datas': datas}
	return render(request=request, template_name="dashboard.html", context=context)

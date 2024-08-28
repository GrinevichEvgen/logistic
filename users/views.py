import logging
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect

from users.forms import RegisterForm, LoginForm
from users.models import User

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        logger.info("POST request received")
        form = LoginForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            user = authenticate(
                request=request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                logger.warning("Authentication failed")
                return HttpResponse("BadRequest", status=400)
            logger.info("User authenticated")
            login(request, user)
            return redirect('driver_list')  # Перенаправление в админку
        else:
            logger.warning("Form is not valid")
            logger.warning(form.errors)  # Отображение ошибок формы
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


def home(request):
    return render(request, 'home.html')

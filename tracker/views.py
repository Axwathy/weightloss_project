from datetime import date

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import WeightForm
from .models import Weight


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def add_weight(request):
    today = date.today()

    already_added = Weight.objects.filter(
        user=request.user,
        date=today
    ).exists()

    if already_added:
        return render(request, "message.html", {
            "message": "You have already added today's weight."
        })

    if request.method == "POST":
        form = WeightForm(request.POST)

        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.date = today
            weight.save()

            return redirect("home")

    else:
        form = WeightForm()

    return render(request, "add_weight.html", {"form": form})


@login_required
def view_weight(request):
    weights = Weight.objects.filter(user=request.user)

    # Search by date
    start = request.GET.get("start")
    end = request.GET.get("end")

    if start and end:
        weights = weights.filter(date__range=[start, end])

    # Latest records first
    weights = weights.order_by("-date")

    # Pagination (5 records per page)
    paginator = Paginator(weights, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "view_weight.html", {
        "page_obj": page_obj
    })


@login_required
def edit_weight(request, id):
    weight = Weight.objects.get(id=id, user=request.user)

    if request.method == "POST":
        form = WeightForm(request.POST, instance=weight)

        if form.is_valid():
            form.save()
            return redirect("view_weight")

    else:
        form = WeightForm(instance=weight)

    return render(request, "add_weight.html", {"form": form})


@login_required
def delete_weight(request, id):
    weight = Weight.objects.get(id=id, user=request.user)

    if request.method == "POST":
        weight.delete()
        return redirect("view_weight")

    return render(request, "delete_weight.html", {"weight": weight})
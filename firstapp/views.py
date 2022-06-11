from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    userForm = UserForm()
    if request.method == "POST":
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            name = userForm.cleaned_data["name"]
            age = userForm.cleaned_data["age"]
            return HttpResponse("<h2>Hello {0}, you are {1} y.o.</h2>".format(name, age))
    return render(request, "index.html", {"form": userForm})

def test(request):
    return render(request,"test.html")

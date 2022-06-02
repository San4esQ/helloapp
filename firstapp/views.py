from django.shortcuts import render

def index(request):
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name" : "Tom", "age" : 23}
    addr = ("Абрикосовая", 23, 45)

    data = {"header":header, "langs":langs, "user":user, "address": addr}
    return render(request, "index.html", context=data)
from django.shortcuts import render

# Create your views here.


def home(request):
    d = {"name": "django", "list": ["alom", "dalim", "akkas", "halim"]}
    return render(request, "home.html", d)


def context(request):
    d = {
        "letters": ["a", "b", "c", "d"],
        "num": 22,
        "quotes": "Hello",
        "greetings": "Its Practice",
        "name": "Prac",
        "status": "",
        "guys": [
            {"name": "dora", "age": 19},
            {"name": "zian", "age": 22},
            {"name": "motu", "age": 31},
        ],
        "file": 123456789,
    }
    return render(request, "context.html", d)
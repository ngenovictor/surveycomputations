from django.shortcuts import render


def index(request):
    template = "index.html"
    title = "Home"
    context = {
        "title": title
    }
    return render(request, template, context)
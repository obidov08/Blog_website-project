from django.shortcuts import render


def about_page(request):
    return render(request, "blog/about.html")


def category_page(request):
    return render(request, "blog/category.html")


def cantact_page(request):
    return render(request, "blog/contact.html")


def index_page(request):
    return render(request, "blog/index.html")


# Create your views here.

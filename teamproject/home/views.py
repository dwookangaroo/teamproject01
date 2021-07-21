from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def board_view(request):
    return render(request, 'index.html')


def compare_view(request):
    return render(request, 'compare.html')

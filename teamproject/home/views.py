from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def board_view(request):
    return render(request, 'index.html')



def usa_view(request):
    return render(request, 'usa.html')


def heinous_view(request):
    return render(request, 'heinous.html')

def compare_view(request):
    return render(request, 'compare.html')
def recidivism_view(request):
    return render(request, 'recidivism.html')


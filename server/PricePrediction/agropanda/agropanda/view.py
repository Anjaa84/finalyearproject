from django.http import HttpResponse
from django.shortcuts import render
import joblib


# def home(request):
#     return HttpResponse("This  is Home")


def home(request):
    return render(request, "home.html")


def result(request):
    cls = joblib.load('finalized_model.sav')

    list = []
    list.append(request.GET['RI'])
    list.append(request.GET['Na'])
    list.append(request.GET['Mg'])
    list.append(request.GET['Al'])
    list.append(request.GET['Si'])
    list.append(request.GET['K'])
    list.append(request.GET['Ca'])
    list.append(request.GET['Ba'])
    list.append(request.GET['Fe'])

    ans = cls.predict([list])

    return render(request, "result.html", {'ans': ans})

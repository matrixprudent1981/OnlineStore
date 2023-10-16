from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def helloView(request):
    return HttpResponse("<h1>Привет это магазин Lucky</h1>")

def now_date_view(request):
    return HttpResponse(f"Сегодня: {datetime.date.today()}")

def goodbyeView(request):
    return HttpResponse("<h1>Good bye user</h1>")
from django.shortcuts import render
import requests
import json

def temp(request):
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=86b2bf5f44df1a3d4f128c2b8f7c15b6")
    x=r.json()
    return render(request, 'temprature.html', {'xolo':x})

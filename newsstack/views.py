from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient

def home_view(request):
    return render(request,"home.html")

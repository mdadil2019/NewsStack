from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def topnews_view(request):
    newsapi = NewsApiClient(api_key='e45eba9d14604d7dabbfbe7f3db2db90')
    top_headlines = newsapi.get_top_headlines(
        category='business',language='en',country='in')


    context = {'articles': top_headlines.get('articles')}
    return render(request,'topnews/topnews.html',context)

def tech_news(request):
    newsapi = NewsApiClient(api_key='e45eba9d14604d7dabbfbe7f3db2db90')
    tech_headlines = newsapi.get_top_headlines(
        category='technology',language='en',country='in')


    context = {'articles': tech_headlines.get('articles')}
    return render(request,'topnews/topnews.html',context)


def sports_news(request):
    newsapi = NewsApiClient(api_key='e45eba9d14604d7dabbfbe7f3db2db90')
    sports_headlines = newsapi.get_top_headlines(
        category='sports',language='en',country='in')


    context = {'articles': sports_headlines.get('articles')}
    return render(request,'topnews/topnews.html',context)

def science_news(request):
    newsapi = NewsApiClient(api_key='e45eba9d14604d7dabbfbe7f3db2db90')
    science_headlines = newsapi.get_top_headlines(
        category='science',language='en',country='in')
    context = {'articles': science_headlines.get('articles')}
    return render(request,'topnews/topnews.html',context)

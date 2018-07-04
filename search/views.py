from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def search_view(request):
    query = request.GET.get('q')
    newsapi = NewsApiClient(api_key='e45eba9d14604d7dabbfbe7f3db2db90')
    top_headlines = newsapi.get_everything(q=query,language='en')
    context = {'articles': top_headlines.get('articles')}
    return render(request,'search/search.html',context)

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
import requests
import json
import re
from newsapi import NewsApiClient

def signup_render(request):
    pass
    
''' The Home Page: Displays the top 
    headlines of what's happening in India.
'''
def home_page(request):
    newsapi = NewsApiClient(api_key='97c1bfdbe1f34677926d62a671bd123b')
    articles = newsapi.get_top_headlines(country='in',page_size=100)
    context={
        'articles':articles,
    }
    return render(request,'home.html',context)

''' The Search Page: Displays the latest 100 
    articles in english from around the world 
    with the entered keyword/phrase.
'''
def search(request):
    if request.method =="POST":        
        newsapi = NewsApiClient(api_key='97c1bfdbe1f34677926d62a671bd123b')
        searched_results = newsapi.get_everything(q=request.POST.get("search"),
                                                  page_size=100,
                                                  language='en',
                                                  sort_by='publishedAt',) #default sort_by is already publishedAt
        context={
            'phrase' : request.POST.get("search"),
            'searched_results':searched_results,
        }
        return render(request,'search.html',context)
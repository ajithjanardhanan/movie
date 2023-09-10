from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Links
#https://github.com/ajithjanardhanan/python.git
# https://github.com/ajithjanardhanan/fashion.git

# Create your views here.
def home(request):
    if request.method=='POST':
        link_new=request.POST.get('page','')
        urls = requests.get(link_new)
        beautifulsoup =BeautifulSoup(urls.text,'html.parser')

        for link in beautifulsoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values=Links.objects.all()
    return  render(request,'home.html',{'data_values':data_values})
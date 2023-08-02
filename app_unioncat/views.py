from django.shortcuts import render
import requests

def home(request):
    response=requests.get('http://localhost:8000/api/books').json()
    return render(request, 'home.html', {'response':response})

def detail(request, id):
    response=requests.get('http://localhost:8000/api/books/{{id}}').json()
    return render(request, 'detail.html', {'response':response})

# Create your views here.

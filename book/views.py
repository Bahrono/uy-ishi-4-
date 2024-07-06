from django.shortcuts import render
from .models import Books, Authors

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def books_view(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def authors_view(request):
    authors = Authors.objects.all()
    return render(request, 'authors.html', {'authors': authors})

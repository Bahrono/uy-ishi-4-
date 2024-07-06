from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('books/', views.books_view, name='books'),
    path('authors/', views.authors_view, name='authors'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('issued/', views.view_issued_books, name='issued_books'),
    path('issue-new/', views.issue_book, name='issue_book'),
]
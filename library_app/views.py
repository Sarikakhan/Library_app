from django.shortcuts import render, redirect
from .models import Book, IssuedBook
from .forms import IssueBookForm
from datetime import date

def home(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'query': query})

def view_issued_books(request):
    issued_list = IssuedBook.objects.all()
    today = date.today()
    
    for item in issued_list:
        if today > item.return_date:
            item.fine = (today - item.return_date).days * 2
        else:
            item.fine = 0
    return render(request, 'issued_books.html', {'issued': issued_list})

def issue_book(request):
    if request.method == "POST":
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('issued_books')
    else:
        form = IssueBookForm()
    return render(request, 'issue_book.html', {'form': form})

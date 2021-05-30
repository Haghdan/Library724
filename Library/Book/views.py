from django.shortcuts import render,get_object_or_404
from .models import Books
from django.core.paginator import Paginator


def all_Books(request):
    all_books=Books.objects.all()
    paginator = Paginator(all_books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Book/all_books.html', {'all_books':all_books,'page_obj': page_obj})

def book_detail(request, id , name):
    book=get_object_or_404(Books,id=id,name=name)    
    return render(request, 'Book/book.html', {'book':book})




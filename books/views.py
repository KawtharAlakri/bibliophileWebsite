from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Book, Review
from books.forms import ReviewForm, BookForm
from books.functions import handle_uploaded_file
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'books/index.html')

def books_list(request):
    book_objects = Book.objects.all()
    return render(request, 'books/all_books.html', {'book_objects': book_objects})

def fiction_list(request):
    book_objects = Book.objects.filter(genre='Fiction')
    return render(request, 'books/fiction_list.html', {'book_objects': book_objects})

def nonfiction_list(request):
    book_objects = Book.objects.filter(genre='Nonfiction')
    return render(request, 'books/Nonfiction_list.html', {'book_objects': book_objects})

def book_detail(request,id):
    book_item = Book.objects.get(id=id)
    reviews = Review.objects.filter(book_item=id)
    return render(request, 'books/book_detail.html',{'book_item': book_item, 'reviews':reviews})

@login_required
def review_form(request,id):
    book_item = Book.objects.get(id=id)
    form = ReviewForm()
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        #if all fields have valid values, get the data and create new Book object
        if form.is_valid():
            review = Review(author=request.user.username,title=form.cleaned_data["title"], body=form.cleaned_data["body"], book_item=book_item)
            review.save()
            return redirect('books:book_detail', id)
    return render(request, 'books/add_review.html',{'book_item': book_item, 'form':form})

@login_required
def add_book(request):
    book_objects = Book.objects.all()
    form = BookForm()
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST, request.FILES)
        #if all fields have valid values, get the data and create new Book object
        if form.is_valid():
            title=form.cleaned_data["title"]
            author=form.cleaned_data["author"]
            description=form.cleaned_data["description"]
            pages = form.cleaned_data["pages"]
            genre=form.cleaned_data["genre"]
            ISBN=form.cleaned_data["ISBN"]

            handle_uploaded_file(request.FILES['cover'])
            coverFileName= request.FILES['cover'].name
            coverPath = "books/{0}".format(coverFileName)

            book = Book(name=title, author=author, desc=description,pages=pages, genre=genre, ISBN=ISBN, cover=coverPath)
            book.save()
            return render(request, 'books/all_books.html', {'book_objects': book_objects})
    return render(request, 'books/add_book.html',{'form':form})

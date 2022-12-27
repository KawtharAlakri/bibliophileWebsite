from django.urls import include, path
from books import views

app_name = "books"
urlpatterns = [
    path('',views.home, name="home"),
    path('books_list',views.books_list, name="books_list"),
    path('fiction_list',views.fiction_list, name="fiction_list"),
    path('nonfiction_list',views.nonfiction_list, name="nonfiction_list"),
    path('books/<int:id>',views.book_detail, name="book_detail"),
    path('review/<int:id>',views.review_form, name="review_form"),
    path('addBook', views.add_book, name = "add_book"),
]

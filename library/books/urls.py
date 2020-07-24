from django.urls import path, reverse, reverse_lazy

from books.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]
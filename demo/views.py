from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
# class Another(View):
#
#     books = Book.objects.filter(is_published=True)# all objects of that model books
#     output = ''
#     for book in books:
#         output += f"We have {book.title} book with ID {book.id} in the database <br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)

# def first(request):
#     return render(request, 'first_temp.html')

class BookViewSet(viewsets.ModelViewSet):
    # create a built-in view for our Books
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)

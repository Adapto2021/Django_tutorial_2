# from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#  class Another(View):
#      #books=Book.objects.all()#Getting all the objects/live data present in the models
#      #books=Book.objects.filter(is_published=True)
#      book=Book.objects.get(id=2)
#      #output=''
#      output="We have {}  book in the database with ID {}".format(book.title,book.id)
#
#      # for book in books:
#      #     output += "We have {}  book in the database with ID {}".format(book.title,book.id)+"<br>"
#
#
#
#     def get(self,request):
#         return HttpResponse(self.output)


def first(request):
#     #return HttpResponse('THis is the first message from views')
   books=Book.objects.all()
   return render(request,'first_temp.html',{'books':books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
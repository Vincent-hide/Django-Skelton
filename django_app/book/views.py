from django.shortcuts import render
from .models import Book

# Create your views here.
def bookHome(request):
    return render(request, "index.html")

def list(request):
    books = Book.objects.all().order_by("price")
    return render(request, "list.html", {
        "books": books
    })

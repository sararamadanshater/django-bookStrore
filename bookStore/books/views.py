from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from django.shortcuts import redirect
# Create your views here.

def index(request):
    books=Book.objects.all()
    return render (request,"books/index.html",{
        "books":books
    })

def create(request):
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ("index")

    return render (request,"books/create.html",{
        "form":form
    })

def edit(request,id):
    book=Book.objects.get(pk=id)
    form=BookForm(request.POST or None ,instance=book)
    if form.is_valid():
        form.save()
        return redirect ("index")

    return render (request,"books/edit.html",{
        "form":form,
        "book":book
    })

def show(request,id):
    book=Book.objects.get(pk=id)
    form=BookForm(request.POST or None ,instance=book)
    if form.is_valid():
        form.save()
        return redirect ("index")

    return render (request,"books/show.html",{
        "form":form,
        "book":book
    })

def delete(request,id):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect ("index")

   


    
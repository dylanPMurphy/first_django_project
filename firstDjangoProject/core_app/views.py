from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to display list of blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def blog_post_id(request, number):
    return HttpResponse("placeholder to display blog number: "+ str(number))

def edit(request, number):
    return HttpResponse("placeholder to edit blog number: "+ str(number))

def destroy(request, number):
    return redirect('/')

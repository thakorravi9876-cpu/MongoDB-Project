from django.shortcuts import render,redirect, get_object_or_404,redirect

# Create your views here.
def home(request):
 return render (request,"home.html")


def master(request):
 return render (request,"master.html")
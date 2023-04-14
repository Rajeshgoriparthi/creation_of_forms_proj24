from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Forms(request):
    if request.method=='POST':
        Fn=request.POST['fn']
        Ln=request.POST['ln']
        Em=request.POST['mail']
        Pw=request.POST['pw']
        return HttpResponse('Data Inserting Successfully...!')
    return render(request,'Forms.html')
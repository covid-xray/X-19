from django.shortcuts import render, redirect

#rendering home page
def home(request):
    return render(request, 'home.html')

#rendering testyourself
def testyourself(request):
    return render(request, 'testyourself.html')

#rendering resources 
def resources(request):
    return render(request, 'resources.html')



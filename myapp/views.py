from django.shortcuts import render, HttpResponse
from myapp.models import Contact
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def codes(request):
    return render(request, 'codes.html')

def snakegame(request):
    return render(request, 'snakegame.html')

def wtrgn(request):
    return render(request, 'wtrgn.html')

def calc(request):
    return render(request, 'calc.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        contact = Contact(name = name, email=email, content = content)
        contact.save()
        
    return render(request, 'contact.html')

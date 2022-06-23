from django.shortcuts import render , HttpResponse
from firstapp.models import Contact
# Create your views here.
def index(request):
    context={
        'variable1':'akash is good',
        'variable2':'rahul is bad'
    }
    return render(request , 'index.html',context)
def about(request):
    return render(request , 'about.html')
def services(request):
    return render(request , 'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact=Contact(name=name,email=email,message=message)
        contact.save()
    return render(request , 'contact.html')
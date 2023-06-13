from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    content = {"page": "Home-Page", "com": "Hussain Icecreams"}
    return render(request, 'index.html', content)

def about(request):
    content = {"page": "About-Page", "com": "Hussain Icecreams"}
    return render(request, 'about.html', content)

def services(request):
    content = {"page": "Services-Page", "com": "Hussain Icecreams"}
    return render(request, 'services.html', content)

def contact(request):
    content = {"page": "Contact-Page", "com": "Hussain Icecreams"}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone, feedback=feedback, date=date)
        contact.save()
        messages.success(request, "Your Message Has Been Sent")
    else:
        messages.error(request, "Your Have Not Sent A Message")

    return render(request, 'contact.html', content)
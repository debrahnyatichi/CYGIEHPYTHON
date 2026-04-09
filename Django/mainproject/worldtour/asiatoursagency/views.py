from django.shortcuts import render, redirect
from .models import Tour
from .forms import ContactForm

# Create your views here.
# def index(request):
#     return render(request, 'tours/index.html')

#This is the home page view function
def home_view(request):
    return render(request, 'tours/home.html')

#This is to define the contact_view function to the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'tours/contact.html', context)

#Define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'tours/contact_success.html')

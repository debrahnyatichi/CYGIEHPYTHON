from django.shortcuts import render, redirect
from .models import Tour
# from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#for class-based views(CBV)
from django.contrib.auth.mixins import LoginRequiredMixin
# for class-based views(CBV)
from django.views import View
#Import the User class
from django.contrib.auth.models import User
#Import the RegisterForm from forms.py
from .forms import RegisterForm


# # Create your views here.
# # def index(request):
# #     return render(request, 'tours/index.html')

# #This is the home page view function
# def home_view(request):
#     return render(request, 'tours/home.html')

# #This is to define the contact_view function to the contact form
# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.send_email()
#             return redirect('contact-success')
#     else:
#         form = ContactForm()
#     context = {'form':form}
#     return render(request, 'tours/contact.html', context)

# #Define the contact_success_view function to handle the success page
# def contact_success_view(request):
#     return render(request, 'tours/contact_success.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
            return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
            return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

#Home View
#using the decorator
@login_required
def home_view(request):
    return render(request, 'home/home.html')

#protected view
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    #'next'- to redirect url
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')
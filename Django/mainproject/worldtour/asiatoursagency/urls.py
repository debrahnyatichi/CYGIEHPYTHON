from django.urls import path
# from .views import index
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.home_view, name="home"),
#  path('contact/', views.contact_view, name="contact"),
#    path('contact/success/', views.contact_success_view, name="contact-success"),
]
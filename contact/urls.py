from django.urls import path
from . import views


urlpatterns = [
    #path("", views.contact, name="contact"),
    path("contact_form/", views.contact_form, name="contact_form"),
]

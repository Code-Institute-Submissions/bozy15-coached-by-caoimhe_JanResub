from django.shortcuts import render
from subscribe.forms import SubscribeForm



def home(request):
    """ View to return the home page """
    #form = SubscribeForm()

    return render(request, "home/index.html",)

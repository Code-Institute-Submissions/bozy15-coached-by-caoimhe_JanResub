from django.shortcuts import render



def home(request):
    """ View to return the home page """
    return render(request, "home/index.html")

from django.shortcuts import render

def about(request):
    """ Renders the about page """
    return render(request, "about/about.html")

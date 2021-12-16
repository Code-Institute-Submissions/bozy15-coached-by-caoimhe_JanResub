from typing import ContextManager
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout, Category

def all_workouts(request):
    """ A view to show all workouts, including sorting and search queries """

    # Get all the available workouts
    workouts = Workout.objects.all()
    # Set query to none to prevent errors
    query = None
    categories = None

    # Checks if request.get exists
    if request.GET:
        # check if category is in request.get
        if "category" in request.GET:
            categories = request.GET['category'].split(',')
            # if it is, filter by category
            workouts = workouts.filter(category__name__in=categories)
            # Filter all categories
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            # Store input in variable
            query = request.GET["q"]
            # If the input is empty
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("workouts"))

            # Filter the workouts by the input in either the name or description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            workouts = Workout.objects.filter(queries)



    # makes everything available in the template
    context = {
        "workouts": workouts,
        "search_term": query, # Pass the search term to the template
        "current_categories": categories, # Pass the list of categories to the template
    }

    return render(request, "workouts/workouts.html", context)

def workout_detail(request, workout_id):
    """ A view to show individual workout details """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, "workouts/workout_detail.html", context)
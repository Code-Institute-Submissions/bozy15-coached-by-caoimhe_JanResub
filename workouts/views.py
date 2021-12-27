from typing import ContextManager
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout, Category
from .forms import WorkoutForm


def all_workouts(request):
    """A view to show all workouts, including sorting and search queries"""

    # Get all the available workouts
    workouts = Workout.objects.all()
    # Set query to none to prevent errors
    query = None
    categories = None

    # Checks if request.get exists
    if request.GET:
        # check if category is in request.get
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
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
        "search_term": query,  # Pass the search term to the template
        "current_categories": categories,  # Pass the list of categories to the template
    }

    return render(request, "workouts/workouts.html", context)


def workout_detail(request, workout_id):
    """A view to show individual workout details"""

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        "workout": workout,
    }

    return render(request, "workouts/workout_detail.html", context)


@login_required
def add_workout(request):
    """Allow superusers to add workouts to the site"""

    # Check if user is a superuser
    if not request.user.is_superuser:
        # If not, redirect to home page
        messages.error(request, "Sorry, only admin can do that!")
        return redirect(reverse("home"))

    # If form is submitted
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = WorkoutForm(request.POST, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # Save the new workout to the database
            workout = form.save()
            # Add a success message
            messages.success(request, "Successfully added new workout!")
            # Redirect to the workout detail page
            return redirect(reverse("workout_detail", args=[workout.id]))
        # If the form is invalid, add an error message
        else:
            messages.error(
                request, "Failed to add workout. Please ensure the form is valid."
            )
    else:  # Get the form
        form = WorkoutForm()

    # The template that will be used
    template = "workouts/add_workout.html"
    # Context that will be passed to the template
    context = {"form": form}

    # Render the template
    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    """Allow superusers to edit workouts"""

    # Check if user is a superuser
    if not request.user.is_superuser:
        # If not, redirect to home page
        messages.error(request, "Sorry, only admin can do that!")
        return redirect(reverse("home"))

    # Get the workout to be edited
    workout = get_object_or_404(Workout, pk=workout_id)

    # If form is submitted
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = WorkoutForm(request.POST, request.FILES, instance=workout)
        # Check if the form is valid
        if form.is_valid():
            # Save the new workout to the database
            form.save()
            # Add a success message
            messages.success(request, "Successfully updated workout!")
            # Redirect to the workout detail page
            return redirect(reverse("workout_detail", args=[workout.id]))
        # If the form is invalid, add an error message
        else:
            messages.error(
                request, "Failed to update workout. Please ensure the form is valid."
            )
    else:  # Get the form
        form = WorkoutForm(instance=workout)
        messages.info(request, f"You are editing {workout.name}")

    # The template that will be used
    template = "workouts/edit_workout.html"
    # Context that will be passed to the template
    context = {"form": form, "workout": workout}

    # Render the template
    return render(request, template, context)

from typing import ContextManager
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout

def all_workouts(request):
    """ A view to show all workouts, including sorting and search queries """

    # Get all the available workouts
    workouts = Workout.objects.all()

    # makes everything available in the template
    context = {
        'workouts': workouts, 
    }

    return render(request, "workouts/workouts.html", context)

def workout_detail(request, workout_id):
    """ A view to show individual workout details """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, "workouts/workout_detail.html", context)
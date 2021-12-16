from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_workouts, name="workouts"), # path to all workouts
    path("<workout_id>", views.workout_detail, name="workout_detail"), # path to workout detail
]

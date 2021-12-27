from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_workouts, name="workouts"), # path to all workouts
    path("<int:workout_id>/", views.workout_detail, name="workout_detail"), # path to workout detail
    path("add/", views.add_workout, name="add_workout"), # path to add workout
]

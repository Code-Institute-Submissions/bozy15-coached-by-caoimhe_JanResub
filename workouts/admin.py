from django.contrib import admin
from .models import Workout, Category, WorkoutReview

class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "description",
        "price",
        "length_of_workout",
        "image",
     )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkoutReview)
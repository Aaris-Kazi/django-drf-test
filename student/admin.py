from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "age",
        "grade",
    ]
    ordering = [
        "id"
    ]
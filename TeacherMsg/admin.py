from django.contrib import admin

from .models import Teacher


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ("name", "sex", "admin", "major", "field", "degree", "title", "depart")


# Register your models here.
admin.site.register(Teacher, TeacherModelAdmin)

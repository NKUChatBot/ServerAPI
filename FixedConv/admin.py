from django.contrib import admin

# Register your models here.
from .models import Aiml


class AimlModelAdmin(admin.ModelAdmin):
    list_display = ("pattern", "template", "that")


admin.site.register(Aiml, AimlModelAdmin)

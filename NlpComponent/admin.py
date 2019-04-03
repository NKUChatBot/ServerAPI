from django.contrib import admin

from .models import WordVector, WordVectorCache


# Register your models here.
class WordVectorModelAdmin(admin.ModelAdmin):
    search_fields = ("word",)
    pass


class WordVectorCacheModelAdmin(admin.ModelAdmin):
    search_fields = ("word",)
    list_display = ("word", "call_times")
    pass


admin.site.register(WordVector, WordVectorModelAdmin)
admin.site.register(WordVectorCache, WordVectorCacheModelAdmin)

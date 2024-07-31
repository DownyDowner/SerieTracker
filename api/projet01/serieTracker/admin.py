from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Utilisateur, Episode, Serie, Suivi, Vu


# Register your models here.

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class SerieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]


admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Suivi)
admin.site.register(Vu)

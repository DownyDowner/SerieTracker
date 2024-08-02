import csv

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse

from .models import Utilisateur, Episode, Serie, Suivi, Vu


# Register your models here.

@admin.action(description='Export selected series and their episodes to CSV')
def export_series_episodes_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="series_episodes.csv"'
    writer = csv.writer(response)

    writer.writerow(['Serie', 'Saison', 'Numéro', 'Nom'])

    for serie in queryset:
        episodes = serie.episodes.all()
        for episode in episodes:
            writer.writerow([serie.nom, episode.saison, episode.episode, episode.nom])

    return response


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class SerieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]
    actions = [export_series_episodes_to_csv]


admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Suivi)
admin.site.register(Vu)

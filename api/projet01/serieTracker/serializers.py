from rest_framework import serializers
from .models import Episode, Serie
from django.contrib.auth import get_user_model


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']


class SerieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive']


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'saison', 'episode', 'nom']


class SerieFullSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive', 'episodes']

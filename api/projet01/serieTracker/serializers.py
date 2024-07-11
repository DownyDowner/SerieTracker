from rest_framework import serializers
from .models import Serie
from django.contrib.auth import get_user_model


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive']

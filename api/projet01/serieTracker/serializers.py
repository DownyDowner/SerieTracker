from rest_framework import serializers
from .models import Episode, Serie, Suivi
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
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive', 'episodes']

    def update(self, instance, validated_data):
        episodes_data = validated_data.pop('episodes', [])
        instance.nom = validated_data.get('nom', instance.nom)
        instance.est_archive = validated_data.get('est_archive', instance.est_archive)
        instance.save()

        existing_ids = [ep.id for ep in instance.episodes.all()]
        new_ids = [item['id'] for item in episodes_data if 'id' in item]

        for episode in instance.episodes.all():
            if episode.id not in new_ids:
                episode.delete()

        # Update or create episodes
        for episode_data in episodes_data:
            if 'id' in episode_data and episode_data['id'] in existing_ids:
                episode = Episode.objects.get(id=episode_data['id'])
                episode.saison = episode_data.get('saison', episode.saison)
                episode.episode = episode_data.get('episode', episode.episode)
                episode.nom = episode_data.get('nom', episode.nom)
                episode.save()
            else:
                new_episode = Episode.objects.create(
                    saison=episode_data['saison'],
                    episode=episode_data['episode'],
                    nom=episode_data['nom'],
                    serie=instance
                )
                instance.episodes.add(new_episode)

        return instance


class SuiviSerializer(serializers.ModelSerializer):
    serie = SerieListSerializer()

    class Meta:
        model = Suivi
        fields = ['id', 'serie']


class SuiviCreationSerializer(serializers.ModelSerializer):
    serie = serializers.PrimaryKeyRelatedField(queryset=Serie.objects.all())

    class Meta:
        model = Suivi
        fields = ['id', 'serie']

    def create(self, validated_data):
        utilisateur = self.context['request'].user
        serie = validated_data['serie']
        suivi, created = Suivi.objects.get_or_create(utilisateur=utilisateur, serie=serie)
        return suivi

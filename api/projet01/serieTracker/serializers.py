from rest_framework import serializers
from .models import Episode, Serie, Suivi, Vu, Utilisateur
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
    id = serializers.IntegerField()

    class Meta:
        model = Episode
        fields = ['id', 'saison', 'episode', 'nom']


class SerieFullSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive', 'episodes']

    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        instance.est_archive = validated_data.get('est_archive', instance.est_archive)
        instance.save()

        episodes_data = validated_data.pop('episodes', [])
        existing_episodes = {e.id: e for e in instance.episodes.all()}

        for episode_data in episodes_data:
            episode_id = episode_data.get('id')
            if episode_id > 0:
                episode = existing_episodes.pop(episode_id, None)
                if episode:
                    episode.saison = episode_data.get('saison', episode.saison)
                    episode.episode = episode_data.get('episode', episode.episode)
                    episode.nom = episode_data.get('nom', episode.nom)
                    episode.save()
            else:
                Episode.objects.create(serie=instance, saison=episode_data.get('saison'),
                                       episode=episode_data.get('episode'), nom=episode_data.get('nom'))

        instance.episodes.filter(id__in=existing_episodes.keys()).delete()

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


class EpisodeWithSeenStatusSerializer(serializers.ModelSerializer):
    vu_id = serializers.SerializerMethodField()
    seen = serializers.SerializerMethodField()
    seen_date = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ['id', 'saison', 'episode', 'nom', 'vu_id', 'seen', 'seen_date']

    def get_vu_id(self, obj):
        user = self.context['request'].user
        vu_instance = Vu.objects.filter(utilisateur=user, episode=obj).first()
        return vu_instance.id if vu_instance else None

    def get_seen(self, obj):
        user = self.context['request'].user
        return Vu.objects.filter(utilisateur=user, episode=obj).exists()

    def get_seen_date(self, obj):
        user = self.context['request'].user
        vu_instance = Vu.objects.filter(utilisateur=user, episode=obj).first()
        return vu_instance.date if vu_instance else None


class SerieWithEpisodesSerializer(serializers.ModelSerializer):
    episodes = EpisodeWithSeenStatusSerializer(many=True)

    class Meta:
        model = Serie
        fields = ['id', 'nom', 'est_archive', 'episodes']


class VuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vu
        fields = ['id', 'episode', 'date']


class UtilisateurListSerializer(serializers.ModelSerializer):
    partage_avec = serializers.SerializerMethodField()

    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'partage_avec']

    def get_partage_avec(self, obj):
        current_user = self.context['request'].user
        return current_user.partage_avec.filter(id=obj.id).exists()

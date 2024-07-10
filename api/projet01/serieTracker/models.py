from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Utilisateur(AbstractUser):
    partage_avec = models.ManyToManyField('self', symmetrical=False, related_name='partage_par')

    def __str__(self):
        return self.username

class Serie(models.Model):
    nom = models.CharField(max_length=100)
    est_archive = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Episode(models.Model):
    saison = models.IntegerField()
    episode = models.IntegerField()
    nom = models.CharField(max_length=100, blank=True, null=True)
    serie = models.ForeignKey(Serie, related_name='episodes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.serie.nom} S{self.saison}E{self.episode}"

class Vu(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('utilisateur', 'episode'),)

    def __str__(self):
        return f"{self.utilisateur} a vu {self.episode}"

class Suivi(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('utilisateur', 'serie'),)

    def __str__(self):
        return f"{self.utilisateur} suit {self.serie}"

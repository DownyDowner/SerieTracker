import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet01.settings')
django.setup()

from serieTracker.models import Utilisateur, Serie, Episode, Vu, Suivi

# Effacer les données existantes
Utilisateur.objects.all().delete()
Serie.objects.all().delete()
Episode.objects.all().delete()
Vu.objects.all().delete()
Suivi.objects.all().delete()

# Utilisateurs
admin = Utilisateur.objects.create_superuser(username='admin', password='admin')
utilisateur1 = Utilisateur.objects.create_user(username='boris', password='test')
utilisateur2 = Utilisateur.objects.create_user(username='vspies', password='test')

# Séries non archivées
walking_dead = Serie.objects.create(nom='The Walking Dead')
prison_break = Serie.objects.create(nom='Prison Break')
game_of_thrones = Serie.objects.create(nom='Game of Thrones')

# Episodes pour chaque série non archivée
episode1_wd = Episode.objects.create(saison=1, episode=1, nom='Episode 1', serie=walking_dead)
episode2_wd = Episode.objects.create(saison=1, episode=2, nom='Episode 2', serie=walking_dead)

episode1_pb = Episode.objects.create(saison=1, episode=1, nom='Episode 1', serie=prison_break)
episode2_pb = Episode.objects.create(saison=1, episode=2, nom='Episode 2', serie=prison_break)

episode1_got = Episode.objects.create(saison=1, episode=1, nom='Episode 1', serie=game_of_thrones)
episode2_got = Episode.objects.create(saison=1, episode=2, nom='Episode 2', serie=game_of_thrones)

# Séries archivées
breaking_bad = Serie.objects.create(nom='Breaking Bad', est_archive=True)
lost = Serie.objects.create(nom='Lost', est_archive=True)

# Episodes pour chaque série archivée
episode1_bb = Episode.objects.create(saison=1, episode=1, nom='Episode 1', serie=breaking_bad)
episode2_bb = Episode.objects.create(saison=1, episode=2, nom='Episode 2', serie=breaking_bad)

episode1_lost = Episode.objects.create(saison=1, episode=1, nom='Episode 1', serie=lost)
episode2_lost = Episode.objects.create(saison=1, episode=2, nom='Episode 2', serie=lost)

# Vues
Vu.objects.create(utilisateur=utilisateur1, episode=episode1_wd)
Vu.objects.create(utilisateur=utilisateur2, episode=episode1_pb)
Vu.objects.create(utilisateur=admin, episode=episode1_got)

# Suivis
Suivi.objects.create(utilisateur=utilisateur1, serie=walking_dead)
Suivi.objects.create(utilisateur=utilisateur2, serie=prison_break)
Suivi.objects.create(utilisateur=admin, serie=game_of_thrones)

# Relations de partage
utilisateur1.partage_avec.add(utilisateur2)
utilisateur2.partage_avec.add(admin)

print("Données initiales créées avec succès!")

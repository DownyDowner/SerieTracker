import os
import django
from datetime import datetime

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
utilisateur2 = Utilisateur.objects.create_user(username='downy', password='test')

# Séries non archivées
walking_dead = Serie.objects.create(nom='The Walking Dead')
prison_break = Serie.objects.create(nom='Prison Break')
game_of_thrones = Serie.objects.create(nom='Game of Thrones')

# Episodes pour chaque série non archivée
# The Walking Dead
Episode.objects.create(saison=1, episode=1, nom='Days Gone Bye', serie=walking_dead)
Episode.objects.create(saison=1, episode=2, nom='Guts', serie=walking_dead)
Episode.objects.create(saison=2, episode=1, nom='What Lies Ahead', serie=walking_dead)
Episode.objects.create(saison=2, episode=2, nom='Bloodletting', serie=walking_dead)

# Prison Break
Episode.objects.create(saison=1, episode=1, nom='Pilot', serie=prison_break)
Episode.objects.create(saison=1, episode=2, nom='Allen', serie=prison_break)
Episode.objects.create(saison=2, episode=1, nom='Manhunt', serie=prison_break)
Episode.objects.create(saison=2, episode=2, nom='Otis', serie=prison_break)

# Game of Thrones
Episode.objects.create(saison=1, episode=1, nom='Winter Is Coming', serie=game_of_thrones)
Episode.objects.create(saison=1, episode=2, nom='The Kingsroad', serie=game_of_thrones)
Episode.objects.create(saison=2, episode=1, nom='The North Remembers', serie=game_of_thrones)
Episode.objects.create(saison=2, episode=2, nom='The Night Lands', serie=game_of_thrones)

# Séries archivées
breaking_bad = Serie.objects.create(nom='Breaking Bad', est_archive=True)
lost = Serie.objects.create(nom='Lost', est_archive=True)

# Episodes pour chaque série archivée
# Breaking Bad
Episode.objects.create(saison=1, episode=1, nom='Pilot', serie=breaking_bad)
Episode.objects.create(saison=1, episode=2, nom='Cat’s in the Bag...', serie=breaking_bad)
Episode.objects.create(saison=2, episode=1, nom='Seven Thirty-Seven', serie=breaking_bad)
Episode.objects.create(saison=2, episode=2, nom='Grilled', serie=breaking_bad)

# Lost
Episode.objects.create(saison=1, episode=1, nom='Pilot, Part 1', serie=lost)
Episode.objects.create(saison=1, episode=2, nom='Pilot, Part 2', serie=lost)
Episode.objects.create(saison=2, episode=1, nom='Man of Science, Man of Faith', serie=lost)
Episode.objects.create(saison=2, episode=2, nom='The Glass Ballerina', serie=lost)

# Suivis
Suivi.objects.create(utilisateur=utilisateur1, serie=walking_dead)
Suivi.objects.create(utilisateur=utilisateur2, serie=prison_break)
Suivi.objects.create(utilisateur=admin, serie=game_of_thrones)


# Vues
def get_episode(nom, saison, episode):
    return Episode.objects.filter(nom=nom, saison=saison, episode=episode).first()


Vu.objects.create(
    utilisateur=utilisateur1,
    episode=get_episode('Days Gone Bye', 1, 1),
    date=datetime(2024, 8, 1, 12, 0)
)
Vu.objects.create(
    utilisateur=utilisateur2,
    episode=get_episode('Pilot', 1, 1),
    date=datetime(2024, 8, 2, 15, 0)
)
Vu.objects.create(
    utilisateur=admin,
    episode=get_episode('Winter Is Coming', 1, 1),
    date=datetime(2024, 8, 3, 18, 0)
)

# Relations de partage
utilisateur1.partage_avec.add(admin)
utilisateur1.partage_avec.add(utilisateur2)
utilisateur2.partage_avec.add(admin)
utilisateur2.partage_avec.add(utilisateur1)

print("Données initiales créées avec succès!")

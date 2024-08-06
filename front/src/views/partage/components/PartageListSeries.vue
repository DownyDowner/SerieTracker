<template>
  <v-card class="fill-height">
    <v-card-title class="mt-1">
      <v-select
        label="Choisir un utilisateur"
        :items="usersList"
        item-value="id"
        item-title="username"
        v-model="userId"
        @update:model-value="loadSeries"
        hide-details
      />
    </v-card-title>
    <v-card-text>
      <v-row v-for="serie in seriesList" :key="serie.id" class="mb-4">
        <v-col cols="12">
          <h1>{{ serie.nom }}</h1>
          <v-expansion-panels variant="accordion">
            <v-expansion-panel
              v-for="(episodes, saison) in groupEpisodesBySeason(
                serie.episodes
              )"
              :key="saison"
            >
              <v-expansion-panel-title>
                Saison {{ saison }}
              </v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-list>
                  <v-list-item v-for="episode in episodes" :key="episode.id">
                    <v-list-item-title>
                      Épisode {{ episode.episode }}
                      {{ episode.nom ? ' - "' + episode.nom + '"' : "" }}
                    </v-list-item-title>
                    <v-list-item-subtitle
                      v-if="episode.seen && episode.seen_date"
                    >
                      {{ formatDate(episode.seen_date) }}
                    </v-list-item-subtitle>
                    <template #prepend>
                      <v-checkbox
                        v-model="episode.seen"
                        class="mr-3"
                        density="comfortable"
                        icon="mdi-pencil"
                        color="primary"
                        readonly
                      />
                    </template>
                  </v-list-item>
                </v-list>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { usePartageStore } from "../../../stores/partage";
import { UtilisateurList } from "../../../models/UtilisateurList";
import { SerieStatus } from "../../../models/SerieStatus";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import { EpisodeStatus } from "../../../models/EpisodeStatus";

const partageStore = usePartageStore();

const usersList: Ref<UtilisateurList[]> = ref([]);
const seriesList: Ref<SerieStatus[]> = ref([]);
const userId = ref<null | number>(null);

type GroupedEpisodes = {
  [key: number]: EpisodeStatus[];
};

onMounted(async () => {
  await loadUsers();
});

const groupEpisodesBySeason = (episodes: EpisodeStatus[]) => {
  return episodes.reduce((acc: GroupedEpisodes, episode: EpisodeStatus) => {
    if (!acc[episode.saison]) {
      acc[episode.saison] = [];
    }
    acc[episode.saison].push(episode);
    return acc;
  }, {});
};

async function loadUsers() {
  try {
    usersList.value = await partageStore.getUtilisateursPartageAvec();
  } catch (error) {
    toast.error("Problème lors de l'affichage des utilisateurs dans le select");
  }
}

async function loadSeries() {
  try {
    if (userId.value)
      seriesList.value = await partageStore.getUserSeriesList(userId.value);
    console.log(userId.value, seriesList.value);
  } catch (error) {
    toast.error("Problème lors de l'affichage des séries");
  }
}

function formatDate(dateString: string) {
  const date = new Date(dateString);

  return date.toLocaleDateString();
}
</script>

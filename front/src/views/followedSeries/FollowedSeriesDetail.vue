<template>
  <v-container>
    <v-row class="my-2" align="center" justify="space-between">
      <v-col cols="6" class="d-flex">
        <v-text-field
          class="ml-3"
          v-model="serieStatus.nom"
          label="Nom de la série"
          hide-details
          readonly
        />
        <v-chip v-if="serieStatus.est_archive" class="ml-2 mt-1" color="red">
          La série est archivée
        </v-chip>
      </v-col>
      <v-col cols="6" class="d-flex justify-end align-center">
        <v-btn class="ma-2" color="grey" @click.stop="close">Retour</v-btn>
      </v-col>
    </v-row>
    <v-expansion-panels variant="accordion">
      <v-expansion-panel v-for="season in uniqueSeasons" :key="season">
        <v-expansion-panel-title> Saison {{ season }} </v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-list>
            <v-list-item
              v-for="episode in getEpisodesBySeason(season)"
              :key="episode.id"
            >
              <v-list-item-title>
                Épisode {{ episode.episode }}
                {{ episode.nom ? ' - "' + episode.nom + '"' : "" }}
              </v-list-item-title>
              <v-list-item-subtitle v-if="episode.seen && episode.seen_date">
                {{ formatDate(episode.seen_date) }}
              </v-list-item-subtitle>
              <template #prepend>
                <v-checkbox
                  v-model="episode.seen"
                  class="mr-3"
                  density="comfortable"
                  icon="mdi-pencil"
                  color="primary"
                  @change="checkBoxChanged(episode)"
                />
              </template>
            </v-list-item>
          </v-list>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref, computed, Ref } from "vue";
import { useSerieStore } from "../../stores/serie";
import { SerieStatus } from "../../models/SerieStatus";
import router from "../../router";
import { NavigationConst } from "../../router/routeConst";
import { EpisodeStatus } from "../../models/EpisodeStatus";
import { Vu } from "../../models/Vu";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

const serieStore = useSerieStore();
const serieStatus: Ref<SerieStatus> = ref(new SerieStatus());

onMounted(async () => {
  await loadSerie();
});

async function loadSerie() {
  const idSerie = router.currentRoute.value.params.id as string;
  serieStatus.value = await serieStore.getFollowedSerieDetail(Number(idSerie));
}

const uniqueSeasons = computed(() => {
  if (!serieStatus.value) return [];
  const seasons = new Set<number>();
  serieStatus.value.episodes.forEach((episode) => seasons.add(episode.saison));
  return Array.from(seasons);
});

const getEpisodesBySeason = (season: number) => {
  if (!serieStatus.value) return [];
  return serieStatus.value.episodes.filter(
    (episode) => episode.saison === season
  );
};

function formatDate(dateString: string) {
  const date = new Date(dateString);

  return date.toLocaleDateString();
}

function close() {
  router.push({ name: NavigationConst.nameFollowed });
}

async function checkBoxChanged(episode: EpisodeStatus) {
  try {
    if (episode.seen) {
      const vu = new Vu();
      vu.episode = episode.id;
      await serieStore.createVu(vu);
    } else {
      if (episode.vu_id) await serieStore.deleteVu(episode.vu_id);
    }
  } catch (err) {
    toast.error("Problème lors de l'ajout ou suppression d'un épisode vu");
  } finally {
    await loadSerie();
  }
}
</script>

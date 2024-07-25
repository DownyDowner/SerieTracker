<template>
  <h1 class="ml-3">{{ nomSerie }}</h1>
  <v-expansion-panels>
    <v-expansion-panel
      v-for="(episodes, saison) in groupedEpisodes"
      :key="saison"
    >
      <v-expansion-panel-title>Saison {{ saison }}</v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-list>
          <v-list-item
            v-for="episode in episodes"
            :key="episode.id"
            :title="`Épisode ${episode.episode}`"
            :subtitle="episode.nom || 'Aucun'"
          ></v-list-item>
        </v-list>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script setup lang="ts">
import { onMounted, Ref, ref, computed } from "vue";
import { useSerieStore } from "../../stores/serie";
import router from "../../router";
import { Episode } from "../../models/Episode";

const serieStore = useSerieStore();

const nomSerie = ref("");
const episodes: Ref<Episode[]> = ref([]);

const groupedEpisodes = computed(() => {
  return episodes.value.reduce((acc: Record<number, Episode[]>, episode) => {
    (acc[episode.saison] = acc[episode.saison] || []).push(episode);
    return acc;
  }, {});
});

onMounted(async () => {
  const idSerie = router.currentRoute.value.params.id as string;
  await serieStore.getSerieById(Number(idSerie));
  if (!serieStore.serie) return;
  nomSerie.value = serieStore.serie?.nom;
  episodes.value = serieStore.serie.episodes;
});
</script>

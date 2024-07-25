<template>
  <v-row class="my-2" align="center" justify="space-between">
    <v-col cols="6">
      <v-text-field
        class="ml-3"
        v-model="nomSerie"
        label="Nom de la série"
        hide-details
      />
    </v-col>
    <v-col cols="6 d-flex justify-end">
      <v-btn
        class="mr-3"
        prepend-icon="mdi-plus-circle"
        color="warning"
        @click.stop="addEpisode"
      >
        Ajouter un épisode
      </v-btn>
    </v-col>
  </v-row>
  <v-expansion-panels variant="accordion">
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
          />
        </v-list>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
  <v-row no-gutters class="mt-2">
    <v-col class="d-flex justify-end align-center">
      <v-btn class="ma-2" color="grey" @click.stop="close">Retour</v-btn>
      <v-btn color="success">Sauvegarder</v-btn>
    </v-col>
  </v-row>
  <EditEpisodeDialog ref="editEpisodeDialog" />
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from "vue";
import { useSerieStore } from "../../stores/serie";
import router from "../../router";
import { Episode } from "../../models/Episode";
import { NavigationConst } from "../../router/routeConst";
import EditEpisodeDialog from "./components/EditEpisodeDialog.vue";

const serieStore = useSerieStore();

const nomSerie = ref("");
const episodes = ref<Episode[]>([]);
const editEpisodeDialog = ref<InstanceType<typeof EditEpisodeDialog> | null>(
  null
);

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

const close = () => {
  serieStore.serie = null;
  router.push({ name: NavigationConst.nameHome });
};

const addEpisode = async () => {
  const episodeToAdd = await editEpisodeDialog.value?.openNew();
  if (episodeToAdd) episodes.value.push(episodeToAdd);
};
</script>

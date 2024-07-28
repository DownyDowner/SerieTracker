<template>
  <v-row class="my-2" align="center" justify="space-between">
    <v-col cols="6" class="d-flex">
      <v-text-field
        class="ml-3"
        v-model="nomSerie"
        label="Nom de la série"
        hide-details
        :readonly="serieStore.serie?.est_archive"
      />
      <v-chip
        v-if="serieStore.serie?.est_archive"
        class="ml-2 mt-1"
        color="red"
      >
        La série est archivée
      </v-chip>
    </v-col>
    <v-col
      v-if="!serieStore.serie?.est_archive"
      cols="6"
      class="d-flex justify-end"
    >
      <v-btn
        class="mr-3"
        prepend-icon="mdi-plus-circle"
        color="warning"
        @click.stop="addEpisode"
      >
        Ajouter un épisode
      </v-btn>
      <v-btn
        class="mr-3"
        prepend-icon="mdi-minus-circle"
        color="error"
        @click.stop="archiveSerie"
      >
        Archiver la série
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
          >
            <template #prepend v-if="!serieStore.serie?.est_archive">
              <v-btn
                class="mr-3"
                density="comfortable"
                icon="mdi-pencil"
                color="primary"
                @click.stop="editEpisode(episode)"
              />
            </template>
          </v-list-item>
        </v-list>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
  <v-row no-gutters class="mt-2">
    <v-col class="d-flex justify-end align-center">
      <v-btn class="ma-2" color="grey" @click.stop="close">Retour</v-btn>
      <v-btn
        v-if="!serieStore.serie?.est_archive"
        color="success"
        @click.stop="save"
        >Sauvegarder</v-btn
      >
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
import { SerieFull } from "../../models/SerieFull";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

const serieStore = useSerieStore();

const isLoading = ref(false);
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
  loadById();
});

const loadById = async () => {
  const idSerie = router.currentRoute.value.params.id as string;
  await serieStore.getSerieById(Number(idSerie));
  if (!serieStore.serie) return;
  nomSerie.value = serieStore.serie?.nom;
  episodes.value = serieStore.serie.episodes;
};

const close = () => {
  serieStore.serie?.est_archive
    ? router.push({ name: NavigationConst.nameArchive })
    : router.push({ name: NavigationConst.nameHome });
  serieStore.serie = null;
};

const addEpisode = async () => {
  const episodeToAdd = await editEpisodeDialog.value?.open();
  if (episodeToAdd) {
    episodes.value.push(episodeToAdd);
    toast.success("L'épisode a été ajouté");
  }
};

const archiveSerie = async () => {
  if (!serieStore.serie?.id) return;
  await serieStore.archive(serieStore.serie.id);
  await router.replace({
    name: NavigationConst.nameSerie,
    params: { id: serieStore.serie.id },
  });
  await loadById();
  toast.success("La série a été archivée");
};

const editEpisode = async (episode: Episode) => {
  const episodeToEdit = await editEpisodeDialog.value?.open(episode);
  if (episodeToEdit) {
    episodeToEdit.id = episode.id;
    const index = episodes.value.findIndex((ep) => ep.id === episode.id);
    if (index !== -1) {
      episodes.value[index] = episodeToEdit;
      toast.success("L'épisode a été modifié");
    }
  }
};

async function save() {
  try {
    isLoading.value = true;
    const serieToUpdate = new SerieFull();
    if (!serieStore.serie) return;
    serieToUpdate.id = serieStore.serie?.id;
    serieToUpdate.est_archive = serieStore.serie.est_archive;
    serieToUpdate.nom = nomSerie.value;
    serieToUpdate.episodes = episodes.value;
    serieStore.updateFull(serieToUpdate);
    router.replace({
      name: NavigationConst.nameSerie,
      params: { id: serieToUpdate.id },
    });
    toast.success("La série a été sauvegardée");
  } catch (err: any) {
    console.error("Impossible de modifier la série", err);
  } finally {
    isLoading.value = false;
  }
}
</script>

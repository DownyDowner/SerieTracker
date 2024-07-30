<template>
  <v-row class="ma-0 pa-0" no-gutters>
    <v-col cols="auto" class="ml-1">
      <v-btn
        prepend-icon="mdi-plus-circle"
        class="ma-2"
        color="warning"
        @click.stop="openNewFollowedSerie"
      >
        <v-tooltip text="Ajouter un suivi" activator="parent" />
        Ajouter
      </v-btn>
    </v-col>
  </v-row>
  <v-row class="mx-1" no-gutters>
    <v-col v-for="serie in series" :key="serie.id" cols="12" md="4">
      <v-card class="ma-1 text-center" :title="serie.nom"></v-card>
    </v-col>
  </v-row>
  <AddFollowedSerieDialog
    ref="addFollowedSerieDialog"
    @on-serie-added="loadFollowedSeries"
  />
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { useSerieStore } from "../../stores/serie";
import { SerieList } from "../../models/SerieList";
import AddFollowedSerieDialog from "./components/AddFollowedSerieDialog.vue";

const serieStore = useSerieStore();

const addFollowedSerieDialog = ref<InstanceType<
  typeof AddFollowedSerieDialog
> | null>(null);
const series: Ref<SerieList[]> = ref([]);

onMounted(async () => {
  await loadFollowedSeries();
});

async function loadFollowedSeries() {
  series.value = await serieStore.followedSeries();
}

function openNewFollowedSerie() {
  addFollowedSerieDialog.value?.open();
}
</script>

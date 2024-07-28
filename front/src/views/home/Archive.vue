<template>
  <v-row class="mx-1" no-gutters>
    <v-col
      v-for="serie in serieStore.archiveSeries"
      :key="serie.id"
      cols="12"
      md="4"
    >
      <v-card class="ma-1 text-center" :title="serie.nom">
        <v-card-actions class="justify-center">
          <v-btn
            prepend-icon="mdi-information-outline"
            color="primary"
            @click.stop="openDetailSerie(serie)"
          >
            Voir plus
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useSerieStore } from "../../stores/serie";
import { SerieList } from "../../models/SerieList";
import { NavigationConst } from "../../router/routeConst";
import router from "../../router";
import "vue3-toastify/dist/index.css";

const serieStore = useSerieStore();

onMounted(async () => {
  await serieStore.getArchiveSeries();
});

function openDetailSerie(model: SerieList) {
  router.push({
    name: NavigationConst.nameSerie,
    params: { id: model.id },
  });
}
</script>

<template>
  <v-row class="mx-1" no-gutters>
    <v-col v-for="serie in series" :key="serie.id" cols="12" md="4">
      <v-card class="ma-1 text-center" :title="serie.nom"></v-card>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { useSerieStore } from "../../stores/serie";
import { SerieList } from "../../models/SerieList";

const serieStore = useSerieStore();

const series: Ref<SerieList[]> = ref([]);

onMounted(async () => {
  series.value = await serieStore.followedSeries();
  console.log(series.value);
});
</script>

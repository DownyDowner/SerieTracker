<template>
  <div>
    <div v-for="serie in serieStore.activeSeries" :key="serie.id">
      {{ serie.nom }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useSerieStore } from "../stores/serie";

const serieStore = useSerieStore();

onMounted(async () => {
  await serieStore.getActiveSeries();
});
</script>

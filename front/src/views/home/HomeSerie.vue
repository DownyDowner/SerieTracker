<template>
  <div>{{ serieStore.serie?.nom }}</div>
</template>
<script setup lang="ts">
import { onMounted } from "vue";
import { useSerieStore } from "../../stores/serie";
import router from "../../router";

const serieStore = useSerieStore();

onMounted(async () => {
  const idSerie = router.currentRoute.value.params.id as string;
  await serieStore.getSerieById(Number(idSerie));
});
</script>

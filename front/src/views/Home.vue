<template>
  <v-row class="ma-1">
    <v-col
      v-for="serie in serieStore.activeSeries"
      :key="serie.id"
      cols="12"
      md="4"
    >
      <v-card>
        <v-card-title class="text-center">{{ serie.nom }}</v-card-title>
        <v-card-actions class="justify-center">
          <v-btn prepend-icon="mdi-information-outline" color="primary">
            Voir plus
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useSerieStore } from "../stores/serie";

const serieStore = useSerieStore();

onMounted(async () => {
  await serieStore.getActiveSeries();
});
</script>

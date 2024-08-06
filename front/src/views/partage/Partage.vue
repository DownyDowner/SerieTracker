<template>
  <v-container>
    <v-row no-gutters>
      <v-col cols="12" md="4" class="px-1 mb-2">
        <PartageListUsers />
      </v-col>
      <v-col cols="12" md="8" class="px-1 mb-2">
        <PartageListSeries />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import PartageListSeries from "./components/PartageListSeries.vue";
import PartageListUsers from "./components/PartageListUsers.vue";
</script>

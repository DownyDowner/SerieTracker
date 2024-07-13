<template>
  <v-row class="ma-0 pa-0" no-gutters>
    <v-col cols="auto" class="ml-1">
      <v-btn
        prepend-icon="mdi-plus-circle"
        class="ma-2"
        color="warning"
        @click.stop="openNewSerie"
      >
        <v-tooltip text="Ajouter une série" activator="parent" />
        Ajouter
      </v-btn>
    </v-col>
  </v-row>
  <v-row class="mx-1" no-gutters>
    <v-col
      v-for="serie in serieStore.activeSeries"
      :key="serie.id"
      cols="12"
      md="4"
    >
      <v-card class="ma-1">
        <v-card-title class="d-flex justify-center align-center">
          <div class="ml-3">{{ serie.nom }}</div>
          <v-btn size="small" icon @click.stop="openEditSerie(serie)">
            <v-tooltip text="Modifier le nom de la série" activator="parent" />
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn prepend-icon="mdi-information-outline" color="primary">
            Voir plus
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
  <EditSerieDialog ref="editSerieDialog" @on-serie-edited="onSerieEdited" />
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useSerieStore } from "../../stores/serie";
import EditSerieDialog from "./components/EditSerieDialog.vue";
import { Serie } from "../../models/Serie";

const serieStore = useSerieStore();

const editSerieDialog = ref<InstanceType<typeof EditSerieDialog> | null>(null);

onMounted(async () => {
  await serieStore.getActiveSeries();
});

function openNewSerie() {
  editSerieDialog.value?.openNew();
}

function openEditSerie(serie: Serie) {
  editSerieDialog.value?.openEdit(serie);
}

async function onSerieEdited() {
  await serieStore.getActiveSeries();
}
</script>

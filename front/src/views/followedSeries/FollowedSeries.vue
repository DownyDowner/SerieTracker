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
    <v-col
      v-for="followedSerie in followedSeries"
      :key="followedSerie.id"
      cols="12"
      md="4"
    >
      <v-card class="ma-1 text-center" :title="followedSerie.serie.nom">
        <v-card-actions class="justify-center">
          <v-btn
            class="mr-3"
            prepend-icon="mdi-minus-circle"
            color="error"
            @click.stop="openDeleteDialog(followedSerie)"
          >
            Supprimer
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
  <AddFollowedSerieDialog
    ref="addFollowedSerieDialog"
    @on-serie-added="loadFollowedSeries"
  />
  <DeleteFollowedSerieDialog
    ref="deleteFollowedSerieDialog"
    @on-serie-delete="loadFollowedSeries"
  />
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { useSerieStore } from "../../stores/serie";
import { Suivi } from "../../models/Suivi";
import AddFollowedSerieDialog from "./components/AddFollowedSerieDialog.vue";
import DeleteFollowedSerieDialog from "./components/DeleteFollowedSerieDialog.vue";

const serieStore = useSerieStore();

const addFollowedSerieDialog = ref<InstanceType<
  typeof AddFollowedSerieDialog
> | null>(null);
const deleteFollowedSerieDialog = ref<InstanceType<
  typeof DeleteFollowedSerieDialog
> | null>(null);
const followedSeries: Ref<Suivi[]> = ref([]);

onMounted(async () => {
  await loadFollowedSeries();
});

async function loadFollowedSeries() {
  followedSeries.value = await serieStore.followedSeries();
}

function openNewFollowedSerie() {
  addFollowedSerieDialog.value?.open();
}

function openDeleteDialog(followedSerie: Suivi) {
  deleteFollowedSerieDialog.value?.open(followedSerie);
}
</script>

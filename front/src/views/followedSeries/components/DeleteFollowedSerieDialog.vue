<template>
  <v-dialog
    v-model="isOpen"
    no-click-animation
    scroll-strategy="close"
    max-width="600"
    persistent
  >
    <v-card>
      <v-toolbar flat dark color="error">
        <v-toolbar-title>Suppression d'un suivi</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon dark @click.stop="close">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <span>
          Voulez-vous vraiment supprimer le suivi suivant :
          <b>{{ suivi?.serie.nom }}</b>
        </span>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-tooltip text="Annuler" location="top">
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
              class="ma-2 px-4"
              color="primary"
              variant="flat"
              size="large"
              @click.stop="close"
            >
              <v-icon left class="mr-2">mdi-close</v-icon>
              Annuler
            </v-btn>
          </template>
        </v-tooltip>
        <v-tooltip text="Supprimer le suivi" location="top">
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
              class="ma-2 px-4"
              color="error"
              variant="flat"
              size="large"
              :disabled="!suivi"
              @click.stop="deleteFollowedSerie"
              :loading="isLoading"
            >
              <v-icon left class="mr-2">mdi-content-save</v-icon>
              Supprimer
            </v-btn>
          </template>
        </v-tooltip>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import { Suivi } from "../../../models/Suivi";
import { useSerieStore } from "../../../stores/serie";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

const serieStore = useSerieStore();

const isOpen = ref(false);
const suivi: Ref<Suivi | null> = ref(null);
const isLoading = ref(false);

const emit = defineEmits<{
  (e: "onSerieDelete"): void;
}>();

const open = (suiviToDelete: Suivi) => {
  suivi.value = suiviToDelete;
  isOpen.value = true;
};

const close = () => {
  isOpen.value = false;
  suivi.value = null;
};

async function deleteFollowedSerie() {
  try {
    isLoading.value = true;
    if (!suivi.value) return;
    await serieStore.deleteFollowedSeries(suivi.value.id);
    toast.success("Le suivi a été supprimé");
    emit("onSerieDelete");
    close();
  } catch (error) {
    toast.error("Problème lors de la suppression du suivi");
  } finally {
    isLoading.value = false;
  }
}

defineExpose({
  open,
});
</script>

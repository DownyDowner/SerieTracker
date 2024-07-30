<template>
  <v-dialog
    v-model="isOpen"
    no-click-animation
    scroll-strategy="close"
    max-width="600"
    max-height="600"
    persistent
  >
    <v-form v-model="isValid" @submit.prevent>
      <v-card min-height="200">
        <v-toolbar flat dark color="primary">
          <v-toolbar-title>Ajout d'un suivi</v-toolbar-title>
          <v-spacer />
          <v-btn icon dark @click.stop="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <v-select
            v-model="serie"
            :items="serieStore.activeSeries"
            item-value="id"
            item-title="nom"
            label="Choisir une série"
            :rules="[(v) => !!v || 'Une série doit être sélectionnée']"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="ma-2 px-4"
            color="primary"
            variant="flat"
            size="large"
            @click.stop="close"
          >
            Annuler
          </v-btn>
          <v-btn
            type="submit"
            class="ma-2 px-4"
            color="success"
            variant="flat"
            size="large"
            :disabled="!isValid"
            :loading="isLoading"
            @click.stop="save"
          >
            Sauvegarder
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useSerieStore } from "../../../stores/serie";
import { SuiviCreation } from "../../../models/SuiviCreation";

const serieStore = useSerieStore();

const isOpen = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const serie = ref<null | number>(null);

onMounted(async () => {
  serieStore.getActiveSeries();
});

const emit = defineEmits<{
  (e: "onSerieAdded"): void;
}>();

const open = () => {
  isOpen.value = true;
};

const close = () => {
  isOpen.value = false;
  serie.value = null;
};

async function save() {
  const suivi = new SuiviCreation();
  if (!serie.value) return;
  suivi.serie = serie.value;
  await serieStore.createFollowedSeries(suivi);
  emit("onSerieAdded");
  close();
}

defineExpose({
  open,
});
</script>

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
          <v-toolbar-title v-if="isNew">Ajout d'une série</v-toolbar-title>
          <v-toolbar-title v-else>Modification d'une série</v-toolbar-title>
          <v-spacer />
          <v-btn icon dark @click.stop="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <v-text-field
            label="Nom de la série"
            placeholder="Entrez le nom"
            v-model="newSerie"
            validate-on="input"
            :rules="requiredRules"
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
            @click.stop="create"
            :loading="isLoading"
          >
            Sauvegarder
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>

<script setup lang="ts">
import { Ref, ref } from "vue";
import { SerieList } from "../../../models/SerieList";
import { useSerieStore } from "../../../stores/serie";

const serieStore = useSerieStore();

const isOpen = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const isNew = ref(false);
const newSerie = ref("");
const requiredRules = [(v: string) => !!v || "Le nom de la série est requis"];
const model: Ref<SerieList | null> = ref(null);

const openNew = () => {
  isNew.value = true;
  isOpen.value = true;
};

const openEdit = (serie: SerieList) => {
  model.value = serie;
  newSerie.value = serie.nom;
  isNew.value = false;
  isOpen.value = true;
};

const close = () => {
  isOpen.value = false;
  newSerie.value = "";
};

const emit = defineEmits<{
  (e: "onSerieEdited", model: SerieList): void;
}>();

function getModel(): SerieList {
  const serie = new SerieList();
  serie.nom = newSerie.value;
  return serie;
}

async function create() {
  try {
    if (!isValid.value) return;
    if (isNew.value) {
      let modelUpdated = getModel();
      modelUpdated = await serieStore.create(modelUpdated);
      emit("onSerieEdited", modelUpdated);
    } else {
      if (!model.value) return;
      model.value.nom = newSerie.value;
      await serieStore.update(model.value);
      emit("onSerieEdited", model.value);
    }
    close();
  } catch (err: any) {
    console.error("Impossible de créer la série", err);
  } finally {
    isLoading.value = false;
  }
}

defineExpose({
  openNew,
  openEdit,
});
</script>

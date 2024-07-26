<template>
  <v-dialog
    v-model="isOpen"
    no-click-animation
    scroll-strategy="close"
    max-width="650"
    max-height="650"
    persistent
  >
    <v-form v-model="isValid" @submit.prevent>
      <v-card min-height="200">
        <v-toolbar flat dark color="primary">
          <v-toolbar-title v-if="isNew">Ajout d'un épisode</v-toolbar-title>
          <v-toolbar-title v-else>Modifier l'épisode</v-toolbar-title>
          <v-spacer />
          <v-btn icon dark @click.stop="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <v-row no-gutters>
            <v-col cols="12" md="6" class="mb-2">
              <v-text-field
                v-model="saison"
                label="Saison"
                type="number"
                :rules="[
                  (v) => !!v || 'La saison est requise',
                  (v) => v > 0 || 'La saison doit être un nombre supérieur à 0',
                ]"
              />
            </v-col>
            <v-col cols="12" md="6" class="mb-2">
              <v-text-field
                v-model="episode"
                label="Épisode"
                type="number"
                :rules="[
                  (v) => !!v || 'L\'épisode est requis',
                  (v) =>
                    v > 0 || 'L\'épisode doit être un nombre supérieur à 0',
                ]"
              />
            </v-col>
          </v-row>
          <v-text-field
            v-model="nom"
            label="Nom de l'épisode (Facultatif)"
            hide-details
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
import { ref } from "vue";
import { Episode } from "../../../models/Episode";

const isOpen = ref(false);
const isValid = ref(false);
const isLoading = ref(false);
const isNew = ref(false);
const saison = ref(0);
const episode = ref(0);
const nom = ref<string | null>(null);

let resolve: (value: Episode | null) => void;

const open = (value?: Episode) => {
  if (value) {
    isNew.value = false;
    saison.value = value.saison;
    episode.value = value.episode;
    nom.value = value.nom;
  } else isNew.value = true;
  isOpen.value = true;
  return new Promise<Episode | null>(function (res) {
    resolve = res;
  });
};

const close = () => {
  isOpen.value = false;
  saison.value = 0;
  episode.value = 0;
  nom.value = null;
  resolve(null);
};

const save = () => {
  const episodeToEdit = new Episode();
  episodeToEdit.saison = saison.value;
  episodeToEdit.episode = episode.value;
  episodeToEdit.nom = nom.value;
  resolve(episodeToEdit);
  close();
};

defineExpose({
  open,
});
</script>

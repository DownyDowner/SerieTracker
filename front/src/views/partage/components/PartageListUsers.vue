<template>
  <v-card title="Partage avec">
    <v-card-text>
      <v-checkbox
        v-for="utilisateur in utilisateursPartageList"
        :key="utilisateur.id"
        :label="utilisateur.username"
        v-model="utilisateur.partage_avec"
        @change="checkboxChanged(utilisateur)"
      />
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { UtilisateurList } from "../../../models/UtilisateurList";
import { usePartageStore } from "../../../stores/partage";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

const partageStore = usePartageStore();

const utilisateursPartageList: Ref<UtilisateurList[]> = ref([]);

onMounted(async () => {
  await loadUsers();
});

async function loadUsers() {
  utilisateursPartageList.value =
    await partageStore.getUtilisateursPartageAvec();
}

async function checkboxChanged(user: UtilisateurList) {
  try {
    if (user.partage_avec) await partageStore.addUserFromShareList(user.id);
    else await partageStore.removeUserFromShareList(user.id);
  } catch (err) {
    toast.error("Erreur lors de la modifcation de la liste de partage");
    await loadUsers();
  }
}
</script>

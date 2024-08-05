<template>
  <v-card title="Partage avec">
    <v-card-text>
      <v-checkbox
        v-for="utilisateur in utilisateursPartageList"
        :key="utilisateur.id"
        :label="utilisateur.username"
        v-model="utilisateur.partage_avec"
      />
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import { UtilisateurList } from "../../../models/UtilisateurList";
import { usePartageStore } from "../../../stores/partage";

const partageStore = usePartageStore();

const utilisateursPartageList: Ref<UtilisateurList[]> = ref([]);

onMounted(async () => {
  await loadUsers();
});

async function loadUsers() {
  utilisateursPartageList.value =
    await partageStore.getUtilisateursPartageAvec();
}
</script>

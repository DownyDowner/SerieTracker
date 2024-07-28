<template>
  <v-app-bar flat class="text-white px-2" color="primary" density="compact">
    <v-row align="center" class="w-100 no-gutters">
      <v-col cols="auto">
        <v-app-bar-title>
          {{ NavigationConst.nomApp }} · {{ currentTitle }}
        </v-app-bar-title>
      </v-col>
      <v-col cols="auto">
        <v-btn @click.stop="home" class="d-flex align-center">
          <v-icon left>mdi-home</v-icon>
          <span>Home</span>
        </v-btn>
      </v-col>
      <v-col cols="auto">
        <v-btn @click.stop="archiveSeries" class="d-flex align-center">
          <v-icon left>mdi-archive</v-icon>
          <span>Séries archivées</span>
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col cols="auto">
        <v-list-item class="d-flex align-center">
          <v-list-item-subtitle>{{ userName }}</v-list-item-subtitle>
        </v-list-item>
      </v-col>
      <v-col cols="auto">
        <v-btn
          v-if="authStore.token"
          icon
          color="white"
          size="small"
          variant="flat"
          @click.stop="logout"
        >
          <v-icon color="primary">mdi-logout</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-app-bar>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { onMounted, watch } from "vue";
import { useAuthenticationStore } from "../stores/authentication";
import { NavigationConst } from "../router/routeConst";

const authStore = useAuthenticationStore();
const router = useRouter();
const currentRoute = useRoute();

const currentTitle = ref("");

const userName = computed(() => {
  return authStore.username;
});

onMounted(() => {
  displayRoute();
});

watch(currentRoute, () => displayRoute());

function displayRoute() {
  currentTitle.value = currentRoute.meta?.title as string;
}

function home() {
  router.push({ name: NavigationConst.nameHome });
}

function archiveSeries() {
  router.push({ name: NavigationConst.nameArchive });
}

async function logout() {
  await authStore.logout();
  router.replace({ name: NavigationConst.nameLogin });
}
</script>

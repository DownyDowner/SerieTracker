<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    temporary
    hide-overlay
    class="d-md-none d-flex"
  >
    <v-list>
      <v-list-item @click="home">
        <v-list-item-icon>
          <v-icon>mdi-home</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="archiveSeries">
        <v-list-item-icon>
          <v-icon>mdi-archive</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Séries archivées</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="followedSeries">
        <v-list-item-icon>
          <v-icon>mdi-check-circle</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Séries Suivies</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="share">
        <v-list-item-icon>
          <v-icon>mdi-share-circle</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Partage</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>{{ userName }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="authStore.token" @click="logout">
        <v-list-item-icon>
          <v-icon>mdi-logout</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Déconnexion</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-app-bar flat color="primary" density="compact">
    <v-row align="center" class="w-100 no-gutters mx-2">
      <v-app-bar-nav-icon @click="drawer = !drawer" class="d-md-none" />
      <v-col cols="auto">
        <v-app-bar-title>
          {{ NavigationConst.nomApp }} · {{ currentTitle }}
        </v-app-bar-title>
      </v-col>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-btn @click.stop="home" class="d-flex align-center">
          <v-icon left>mdi-home</v-icon>
          <span>Home</span>
        </v-btn>
      </v-col>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-btn @click.stop="archiveSeries" class="d-flex align-center">
          <v-icon left>mdi-archive</v-icon>
          <span>Séries archivées</span>
        </v-btn>
      </v-col>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-btn @click.stop="followedSeries" class="d-flex align-center">
          <v-icon left>mdi-check-circle</v-icon>
          <span>Séries Suivies</span>
        </v-btn>
      </v-col>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-btn @click.stop="share" class="d-flex align-center">
          <v-icon left>mdi-share-circle</v-icon>
          <span>Partage</span>
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-list-item class="d-flex align-center">
          <v-list-item-subtitle>{{ userName }}</v-list-item-subtitle>
        </v-list-item>
      </v-col>
      <v-col cols="auto" class="d-none d-md-flex">
        <v-btn
          v-if="authStore.token"
          icon
          color="white"
          size="small"
          variant="flat"
          @click.stop="logout"
          data-cy="logout-button"
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
const drawer = ref(false);

const userName = computed(() => authStore.username);

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

function followedSeries() {
  router.push({ name: NavigationConst.nameFollowed });
}

function share() {
  router.push({ name: NavigationConst.nameShare });
}

async function logout() {
  await authStore.logout();
  router.replace({ name: NavigationConst.nameLogin });
}
</script>

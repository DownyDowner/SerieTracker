<template>
  <v-app-bar flat class="text-white" color="primary" density="compact">
    <v-app-bar-title>
      {{ NavigationConst.nomApp }} · {{ currentTitle }}
    </v-app-bar-title>
    <template v-slot:append>
      <v-list-item>
        <v-list-item-subtitle>{{ userName }}</v-list-item-subtitle>
      </v-list-item>
      <v-btn
        v-if="authStore.token"
        icon
        color="white"
        size="small"
        class="ml-3"
        variant="flat"
        @click.stop="logout"
      >
        <v-icon icon="mdi-logout" color="primary" />
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { onMounted } from "vue";
import { watch } from "vue";
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

async function logout() {
  await authStore.logout();
  router.push({ name: NavigationConst.nameLogin });
}
</script>

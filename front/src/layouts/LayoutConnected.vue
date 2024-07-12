<template>
  <v-app>
    <nav-bar-vue />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import NavBarVue from "../components/NavBar.vue";
</script>

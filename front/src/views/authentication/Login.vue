<template>
  <v-container
    fluid
    class="align-start border-app"
    style="max-width: 500px; max-height: 500px"
  >
    <v-card rounded="lg" style="max-width: 400px" class="mx-auto my-auto">
      <v-card-title style="word-break: keep-all">
        <h2 class="text-primary text-center">Connexion</h2>
        <h4 class="text-center mt-2">Veuillez entrer vos identifiants</h4>
      </v-card-title>
      <v-card-text class="mt-5">
        <v-form v-model="isValid">
          <v-text-field
            class="mb-2"
            label="Nom d'utilisateur"
            rounded="lg"
            prepend-inner-icon="mdi-account"
            v-model="authModel.username"
            autofocus
            :rules="stringRules"
            data-cy="username-input"
          />
          <v-text-field
            class="mb-2"
            label="Mot de passe"
            rounded="lg"
            prepend-inner-icon="mdi-lock"
            :append-inner-icon="showPassword ? `mdi-eye` : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            v-model="authModel.password"
            :rules="stringRules"
            @keypress.enter="login"
            @click:append-inner="showPassword = !showPassword"
            data-cy="password-input"
          />
        </v-form>

        <v-btn
          color="primary"
          block
          :disabled="!isValid"
          @click="login"
          data-cy="login-button"
        >
          Connexion
        </v-btn>
        <v-btn
          @click.stop="createAccount"
          color="grey-lighten-3 mt-1"
          variant="flat"
          block
          data-cy="create-account-button"
        >
          Créer un compte
        </v-btn>
      </v-card-text>
      <v-alert
        v-if="authModel.errorMessages"
        type="error"
        class="mt-2"
        dismissible
        data-cy="error-message"
      >
        {{ authModel.errorMessages }}
      </v-alert>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import router from "../../router";
import { NavigationConst } from "../../router/routeConst";
import { useAuthenticationStore } from "../../stores/authentication";

const authStore = useAuthenticationStore();

const stringRules = ref<any[]>([(v: string) => !!v || "Valeur obligatoire"]);
const showPassword = ref<boolean>(false);
const isValid = ref<boolean>(true);

const authModel = reactive({
  username: "",
  password: "",
  errorMessages: "",
});

async function login() {
  try {
    await authStore.login(authModel.username, authModel.password);
    router.push({ name: NavigationConst.nameHome });
  } catch (err) {
    authModel.errorMessages =
      "Échec de la connexion. Veuillez vérifier vos identifiants et réessayer";
    authModel.password = "";
  }
}

function createAccount() {
  router.push({ name: NavigationConst.nameSignUp });
}
</script>

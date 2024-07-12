import { computed, ref, Ref } from 'vue';
import { defineStore } from 'pinia';
import { AuthApi } from '../apis/AuthApi';

export const useAuthenticationStore = defineStore('authentication', () => {
  const token: Ref<string> = ref(localStorage.getItem('Auth-Token') || '');
  const user = ref<any | null>(null);
  const username = computed(() => user.value?.username);

  const loading = ref<boolean>(false);

  async function login(username: string, password: string): Promise<void> {
    try {
      loading.value = true;
      token.value = await AuthApi.login(username, password);
      localStorage.setItem('Auth-Token', token.value);
    } catch (error) {
      console.error('Error while logging in:', error);
      throw error;
    } finally {
      loading.value = false;
    }
  }

  async function signup(username: string, password: string): Promise<void> {
    try {
      loading.value = true;
      token.value = await AuthApi.signup(username, password);
      localStorage.setItem('Auth-Token', token.value);
    } catch (error) {
      console.error('Error while logging in:', error);
      throw error;
    } finally {
      loading.value = false;
    }
  }

  async function logout() {
    try {
      loading.value = true
      await AuthApi.logout();
    }catch (error) {
      console.error('Error while logging in:', error);
      throw error;
    } finally {
      loading.value = false;
    }
  }

  async function loadUser(): Promise<void> {
    if (!token.value) {
      user.value = null;
      return;
    }
    try {
      const userData = await AuthApi.getUser(token.value);
      user.value = userData;
    } catch (error) {
      console.error('Error fetching user:', error);
      resetToken();
    }
  }

  function resetToken() : void {
    token.value = '';
    user.value = null;
  }

  return {
    loading,
    token,
    user,
    username,
    login,
    signup,
    logout,
    loadUser,
  };
});

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
      console.log('token', token.value)
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

  return {
    loading,
    token,
    user,
    username,
    login,
    signup,
  };
});

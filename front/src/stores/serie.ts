import { ref, Ref } from 'vue';
import { defineStore } from "pinia";
import { Serie } from '../models/Serie';
import { SerieApi } from '../apis/SerieApi';

export const useSerieStore = defineStore('serie', () => {

  const isLoading = ref(false);
  const activeSeries: Ref<Serie[]> = ref([]);

  async function getActiveSeries(): Promise<void> {
    try {
      isLoading.value = true;
      activeSeries.value = await SerieApi.getActiveSeries();
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function create(serie: Serie) {
    try {
      isLoading.value = true;
      serie = await SerieApi.create(serie)
      return serie
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  return {
    isLoading,
    activeSeries,
    getActiveSeries,
    create,
  };
});

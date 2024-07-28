import { SerieList } from '../models/SerieList';
import { ref, Ref } from 'vue';
import { defineStore } from "pinia";
import { SerieApi } from '../apis/SerieApi';
import { SerieFull } from '../models/SerieFull';

export const useSerieStore = defineStore('serie', () => {

  const isLoading = ref(false);
  const activeSeries: Ref<SerieList[]> = ref([]);
  const archiveSeries: Ref<SerieList[]> = ref([]);
  const serie: Ref<SerieFull | null> = ref(null);

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

  async function getArchiveSeries(): Promise<void> {
    try {
      isLoading.value = true;
      archiveSeries.value = await SerieApi.getArchiveSeries();
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function getSerieById(id: number) {
    try {
      isLoading.value = true;
      serie.value = await SerieApi.getById(id);
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function create(serie: SerieList) {
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

  async function update(serie: SerieList) {
    try {
      isLoading.value = true;
      await SerieApi.update(serie)
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function updateFull(serie: SerieFull) {
    try {
      isLoading.value = true;
      await SerieApi.updateFull(serie)
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function archive(id: number) {
    try {
      isLoading.value = true;
      await SerieApi.archive(id)
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
    archiveSeries,
    serie,
    getActiveSeries,
    getArchiveSeries,
    getSerieById,
    create,
    update,
    updateFull,
    archive,
  };
});

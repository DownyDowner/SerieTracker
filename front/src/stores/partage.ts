import { defineStore } from "pinia";
import { ref } from "vue";
import { PartageApi } from "../apis/PartageApi";

export const usePartageStore = defineStore('partage', () => {

    const isLoading = ref(false);
    
    async function getUtilisateursPartageAvec() {
        try {
            isLoading.value = true
            return await PartageApi.getUtilisateursPartageAvec()
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }
  
    return {
        getUtilisateursPartageAvec
    };
  });
  
import { defineStore } from "pinia";
import { ref } from "vue";
import { PartageApi } from "../apis/PartageApi";

export const usePartageStore = defineStore('partage', () => {

    const isLoading = ref(false);
    
    async function getAllUsers() {
        try {
            isLoading.value = true
            return await PartageApi.getAllUsers()
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }

    async function addUserFromShareList(id: number) {
        try {
            isLoading.value = true
            await PartageApi.addUserFromShareList(id)
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }

    async function removeUserFromShareList(id: number) {
        try {
            isLoading.value = true
            await PartageApi.removeUserFromShareList(id)
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }

    async function getSharedUsers() {
        try {
            isLoading.value = true
            return await PartageApi.getSharedUsers()
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }

    async function getUserSeriesList(id: number) {
        try {
            isLoading.value = true
            return await PartageApi.getUserSeriesList(id)
        } catch (error) {
            console.error(error);
            throw error;
        } finally {
            isLoading.value = false
        }
    }
  
    return {
        getAllUsers,
        addUserFromShareList,
        removeUserFromShareList,
        getSharedUsers,
        getUserSeriesList,
    };
  });
  
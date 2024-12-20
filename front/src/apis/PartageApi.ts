import axios from "axios";
import { UtilisateurList, UtilisateurListDTO } from "../models/UtilisateurList";
import { useAuthenticationStore } from "../stores/authentication";
import { SerieStatus, SerieStatusDTO } from "../models/SerieStatus";

export abstract class PartageApi {
    static API_URL = "http://localhost:8000/partage/";
    static authStore = useAuthenticationStore()

    static async getAllUsers(): Promise<UtilisateurList[]> {
        const response = await axios.get<UtilisateurListDTO[]>(`${PartageApi.API_URL}all-users/` , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
        
        return response.data.map(d => new UtilisateurList(d));
    }

    static async addUserFromShareList(userId: number): Promise<void> {
        await axios.post(`${PartageApi.API_URL}add/${userId}/`, {} , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async removeUserFromShareList(userId: number): Promise<void> {
        await axios.post(`${PartageApi.API_URL}remove/${userId}/`, {} , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async getSharedUsers(): Promise<UtilisateurList[]> {
        const response = await axios.get<UtilisateurListDTO[]>(`${PartageApi.API_URL}` , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
        
        return response.data.map(d => new UtilisateurList(d));
    }

    static async getUserSeriesList(userId: number): Promise<SerieStatus[]> {
        const response = await axios.get<SerieStatusDTO[]>(`${PartageApi.API_URL}${userId}/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return response.data.map(d => new SerieStatus(d));
    }
}
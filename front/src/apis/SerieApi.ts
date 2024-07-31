import axios from "axios";
import { SerieList, SerieListDTO } from "../models/SerieList";
import { useAuthenticationStore } from "../stores/authentication";
import { SerieFull, SerieFullDTO } from "../models/SerieFull";
import { Suivi, SuiviDTO } from "../models/Suivi";
import { SuiviCreation, SuiviCreationDTO } from "../models/SuiviCreation";
import { SerieStatus, SerieStatusDTO } from "../models/SerieStatus";

export abstract class SerieApi {
    static API_URL = "http://localhost:8000/series/";
    static authStore = useAuthenticationStore()
  
    static async getActiveSeries(): Promise<SerieList[]> {
        const response = await axios.get<SerieListDTO[]>(`${SerieApi.API_URL}active/` , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
        
        return response.data.map(d => new SerieList(d));
    }

    static async getArchiveSeries(): Promise<SerieList[]> {
        const response = await axios.get<SerieListDTO[]>(`${SerieApi.API_URL}archive/` , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
        
        return response.data.map(d => new SerieList(d));
    }

    static async getById(id: number): Promise<SerieFull> {
        const response = await axios.get<SerieFullDTO>(`${SerieApi.API_URL}${id}/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new SerieFull(response.data)
    }

    static async create(serie: SerieList) : Promise<SerieList> {
        const response = await axios.post<SerieListDTO>(SerieApi.API_URL, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new SerieList(response.data);
    }

    static async update(serie: SerieList) {
        await axios.put<SerieListDTO>(`${SerieApi.API_URL}${serie.id}/update/`, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async updateFull(serie: SerieFull) {
        await axios.put<SerieFullDTO>(`${SerieApi.API_URL}${serie.id}/update-episodes/`, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async archive(id: number) {
        await axios.delete(`${SerieApi.API_URL}${id}/archive/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async followedSeries(): Promise<Suivi[]> {
        const response = await axios.get<SuiviDTO[]>(`${SerieApi.API_URL}suivies/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return response.data.map(d => new Suivi(d));
    }

    static async createFollowedSeries(suivi: SuiviCreation): Promise<SuiviCreation> {
        const response = await axios.post<SuiviCreationDTO>(`${SerieApi.API_URL}suivies-create/`, suivi, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new SuiviCreation(response.data);
    }

    static async deleteFollowedSeries(id: number): Promise<void> {
        await axios.delete(`${SerieApi.API_URL}suivies-delete/${id}/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }

    static async getFollowedSerieDetail(id: number): Promise<SerieStatus> {
        const response = await axios.get<SerieStatusDTO>(`${SerieApi.API_URL}suivies/${id}/`, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new SerieStatus(response.data)
    }
}
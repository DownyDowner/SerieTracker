import axios from "axios";
import { SerieList, SerieListDTO } from "../models/SerieList";
import { useAuthenticationStore } from "../stores/authentication";

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

    static async create(serie: SerieList) : Promise<SerieList> {
        const response = await axios.post<SerieListDTO>(SerieApi.API_URL, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new SerieList(response.data);
    }

    static async update(serie: SerieList) {
        await axios.put<SerieListDTO>(`${SerieApi.API_URL}${serie.id}/`, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
    }
}
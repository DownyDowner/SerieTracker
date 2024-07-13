import axios from "axios";
import { Serie, SerieDTO } from "../models/Serie";
import { useAuthenticationStore } from "../stores/authentication";

export abstract class SerieApi {
    static API_URL = "http://localhost:8000/series/";
    static authStore = useAuthenticationStore()
  
    static async getActiveSeries(): Promise<Serie[]> {
        const response = await axios.get<SerieDTO[]>(`${SerieApi.API_URL}active/` , {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });
        
        return response.data.map(d => new Serie(d));
    }

    static async create(serie: Serie) : Promise<Serie> {
        const response = await axios.post<SerieDTO>(SerieApi.API_URL, serie, {
            headers: { 'Authorization': 'Token ' + this.authStore.token },
            responseType: 'json',
        });

        return new Serie(response.data);
    }
}
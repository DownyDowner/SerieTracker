import axios from "axios";
import { Serie, SerieDTO } from "../models/Serie";

export abstract class SerieApi {
    static API_URL = "http://localhost:8000/series/";
  
    static async getActiveSeries(): Promise<Serie[]> {
        const response = await axios.get<SerieDTO[]>(`${SerieApi.API_URL}active/`);
        
        return response.data.map(d => new Serie(d));
    }
}
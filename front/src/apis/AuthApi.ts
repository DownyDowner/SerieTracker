import axios from "axios";

export abstract class AuthApi {
    static API_URL = "http://localhost:8000/api-auth/";
  
    static async login(username: string, password: string) {
        const response = await axios.post(`${AuthApi.API_URL}login/`, {
          username,
          password,
        });
        return response.data;
    }
    
    static async signup(username: string, password: string) {
        const response = await axios.post(`${AuthApi.API_URL}signup/`, {
          username,
          password,
        });
        return response.data;
    }
}
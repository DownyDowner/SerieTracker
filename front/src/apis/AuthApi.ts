import axios from "axios";

export abstract class AuthApi {
    static API_URL = "http://localhost:8000/api-auth";
  
    static async login(username: string, password: string): Promise<string> {
        const response = await axios.post(`${AuthApi.API_URL}/login/`, {
          username,
          password,
        });
        return response.data;
    }
    
    static async signup(username: string, password: string): Promise<string> {
        const response = await axios.post(`${AuthApi.API_URL}/signup/`, {
          username,
          password,
        });
        return response.data;
    }

    static async logout(): Promise<void> {
      const token = localStorage.getItem('Auth-Token');
      if (!token) {
        return;
      }

      try {
        await axios.post(`${AuthApi.API_URL}/logout/`, {}, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        localStorage.removeItem('Auth-Token');
      } catch (error) {
        console.error('Error logging out:', error);
        throw error;
      }
    }

    static async getUser(token: string) {
      const response = await axios.get(`${AuthApi.API_URL}/user/`, {
        headers: {
          'Authorization': `Token ${token}`
        }
      });

      return response.data;
    }
}
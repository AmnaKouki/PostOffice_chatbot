import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class ChatbotService {
  constructor(private http: HttpClient) {}

  sendMessage(str: String, senderId: String) {
    return this.http.post(environment.apiUrl, {
      message: str,
      sender: senderId,
    });
  }
}

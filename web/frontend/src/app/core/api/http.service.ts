import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  get apiUrl(): string {
    return environment.apiUrl;
  }

  constructor(private _http: HttpClient) { }

  get(endpoint: string, options?): Observable<any> {
    return this._http.get(`${this.apiUrl}/${endpoint}`, options);
  }

  post(endpoint: string, data, options?): Observable<any> {
    return this._http.post(`${this.apiUrl}/${endpoint}`, data, options);
  }

  put(endpoint: string, data, options?): Observable<any> {
    return this._http.put(`${this.apiUrl}/${endpoint}`, data, options);
  }

  delete(endpoint: string, options?): Observable<any> {
    return this._http.delete(`${this.apiUrl}/${endpoint}`, options);
  }
}
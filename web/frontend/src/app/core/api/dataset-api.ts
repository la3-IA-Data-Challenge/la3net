import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpService } from './http.service';

@Injectable({
    providedIn: 'root'
})
export class DatasetApi {
    private readonly apiController: string = 'datasets';

    constructor(private api: HttpService) { }

    list(): Observable<any> {
        return this.api.get(`${this.apiController}/list/`);
    }

    get(id: number): Observable<any> {
        return this.api.get(`${this.apiController}/${id}/`);
    }

    add(item: any): Observable<any> {
        return this.api.post(this.apiController, item);
    }
}

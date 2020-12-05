import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DatasetApi } from '../api/dataset-api';
import { Dataset, DatasetData } from '../interface/dataset';

@Injectable({
  providedIn: 'root'
})
export class DatasetsService extends DatasetData {

  constructor(private api: DatasetApi) {
    super();
  }

  list(): Observable<Dataset[]> {
    return this.api.list();
  }

  get(id: number): Observable<Dataset> {
    return this.api.get(id);
  }

  add(dataset: any): Observable<Dataset> {
    return this.api.add(dataset);
  }
}

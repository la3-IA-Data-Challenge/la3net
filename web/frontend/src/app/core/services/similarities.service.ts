import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { SimilarityApi } from '../api/similarity-api';
import { Similarity, SimilarityData } from '../interface/similarity';

@Injectable({
  providedIn: 'root'
})
export class SimilaritiessService extends SimilarityData {

  constructor(private api: SimilarityApi) {
    super();
  }

  list(): Observable<Similarity[]> {
    return this.api.list();
  }

  get(id: number): Observable<Similarity> {
    return this.api.get(id);
  }

  add(similarity: any): Observable<Similarity> {
    return this.api.add(similarity);
  }

  execute(item: any): Observable<Similarity> {
    return this.api.execute(item);
  }

}

import { Observable } from 'rxjs';
import { Dataset } from './dataset';
import { File } from './file';

export interface Similarity {
    id: number;
    targets: File[];
    results: File[];
    dataset: Dataset;
}

export abstract class SimilarityData {
    abstract list(): Observable<Similarity[]>;
    abstract get(id: number): Observable<Similarity>;
    abstract add(similarity: any): Observable<Similarity>;
    abstract execute(item: any): Observable<Similarity>;
}
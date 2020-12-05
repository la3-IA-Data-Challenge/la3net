import { Observable } from 'rxjs';
import { File } from './file';

export interface Dataset {
    id: number;
    files: File[];
}

export abstract class DatasetData {
    abstract list(): Observable<Dataset[]>;
    abstract get(id: number): Observable<Dataset>;
    abstract add(dataset: Dataset): Observable<Dataset>;
}
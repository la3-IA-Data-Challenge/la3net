import { Observable } from 'rxjs';

export interface File {
    id: number;
    file: string;
}

export abstract class FileData {
    abstract list(): Observable<File[]>;
    abstract get(id: number): Observable<File>;
    abstract add(file: File): Observable<File>;
}
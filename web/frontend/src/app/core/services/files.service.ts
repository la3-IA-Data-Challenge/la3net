import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { FileApi } from '../api/file-api';
import { File, FileData } from '../interface/file';

@Injectable({
  providedIn: 'root'
})
export class FilesService extends FileData {

  constructor(private api: FileApi) {
    super();
  }

  list(): Observable<File[]> {
    return this.api.list();
  }

  get(id: number): Observable<File> {
    return this.api.get(id);
  }

  add(file: any): Observable<File> {
    return this.api.add(file);
  }
}

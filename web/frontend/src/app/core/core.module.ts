import { ModuleWithProviders, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';

import { DatasetApi } from './api/dataset-api';
import { FileApi } from './api/file-api';
import { SimilarityApi } from './api/similarity-api';
import { DatasetData } from './interface/dataset';
import { DatasetsService } from './services/datasets.service';
import { FileData } from './interface/file';
import { FilesService } from './services/files.service';
import { SimilarityData } from './interface/similarity';
import { SimilaritiessService } from './services/similarities.service';

const API = [
  DatasetApi,
  FileApi,
  SimilarityApi
];

const SERVICES = [
  { provide: DatasetData, useClass: DatasetsService },
  { provide: FileData, useClass: FilesService },
  { provide: SimilarityData, useClass: SimilaritiessService },
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken'
    })
  ]
})
export class CoreModule {
  static forRoot(): ModuleWithProviders<CoreModule> {
    return {
      ngModule: CoreModule,
      providers: [
        ...API,
        ...SERVICES,
      ],
    };
  }
}

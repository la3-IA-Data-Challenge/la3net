import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { Dataset, DatasetData } from 'src/app/core/interface/dataset';
import { File } from 'src/app/core/interface/file';
import { Similarity, SimilarityData } from 'src/app/core/interface/similarity';

@Component({
  selector: 'app-select-targets',
  templateUrl: './select-targets.component.html',
  styleUrls: ['./select-targets.component.scss']
})
export class SelectTargetsComponent implements OnInit, OnDestroy {

  protected readonly unsubscribe$ = new Subject<void>();

  dataset: Dataset;
  datasetId: number;

  similarity: Similarity;

  availableFiles: File[];
  selectedFiles: File[];
  draggedFile: File;

  pageFiles: File[];
  page: number = 0;
  rows: number = 10;

  constructor(
    private route: ActivatedRoute,
    private datasetsServices: DatasetData,
    private similaritiesServices: SimilarityData,
    private router: Router,
  ) { }

  ngOnInit(): void {
    this.route.params.pipe(takeUntil(this.unsubscribe$)).subscribe(
      (params) => {
        this.datasetId = +params['id'];
        this.datasetsServices.get(this.datasetId).pipe(takeUntil(this.unsubscribe$)).subscribe(
          (res) => {
            this.dataset = res;
            this.availableFiles = this.dataset.files;
            this.pageFiles = this.availableFiles.slice(this.page * this.rows, this.page * this.rows + this.rows);
          }
        )
      }
    )

    this.selectedFiles = [];
  }

  select(event, file: File) {
    let draggedFileIndex = this.availableFiles.findIndex(x => x.id === file.id);
    this.selectedFiles = [...this.selectedFiles, file];
    this.availableFiles = this.availableFiles.filter((val, i) => i != draggedFileIndex);

    this.pageFiles = this.availableFiles.slice(this.page * this.rows, this.page * this.rows + this.rows);
  }

  deselect(event, file: File) {
    let draggedFileIndex = this.selectedFiles.findIndex(x => x.id === file.id);
    this.availableFiles = [...this.availableFiles, file];
    this.selectedFiles = this.selectedFiles.filter((val, i) => i != draggedFileIndex);

    this.pageFiles = this.availableFiles.slice(this.page * this.rows, this.page * this.rows + this.rows);
  }


  findIndex(file: File) {
    let index = -1;
    for (let i = 0; i < this.availableFiles.length; i++) {
      if (file.id === this.availableFiles[i].id) {
        index = i;
        break;
      }
    }
    return index;
  }

  paginate(event) {
    this.page = event.page;
    this.rows = event.rows;
    this.pageFiles = this.availableFiles.slice(this.page * this.rows, this.page * this.rows + this.rows);
  }

  goToNextStep(event) {

    let targets: number[] = []
    this.selectedFiles.forEach(element => {
      targets.push(element.id);
    });

    let similarity = {
      id: 0,
      dataset: this.dataset.id,
      targets: targets,
      results: [],
    }

    this.similaritiesServices.add(similarity).pipe(takeUntil(this.unsubscribe$)).subscribe(
      (res: Similarity) => {
        this.router.navigate(['step3/', res.id]);
      },
      (err) => {
        console.error(err);
      }
    )
  }

  ngOnDestroy(): void {
    //Called once, before the instance is destroyed.
    //Add 'implements OnDestroy' to the class.
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }
}

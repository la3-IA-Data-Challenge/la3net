import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { Dataset, DatasetData } from 'src/app/core/interface/dataset';
import { SimilarityData } from 'src/app/core/interface/similarity';

@Component({
  selector: 'app-select-targets',
  templateUrl: './select-targets.component.html',
  styleUrls: ['./select-targets.component.scss']
})
export class SelectTargetsComponent implements OnInit, OnDestroy {

  protected readonly unsubscribe$ = new Subject<void>();

  dataset: Dataset;
  datasetId: number;

  constructor(
    private route: ActivatedRoute,
    private datasetsServices: DatasetData,
    private similaritiesServices: SimilarityData
  ) { }

  ngOnInit(): void {
    this.route.params.pipe(takeUntil(this.unsubscribe$)).subscribe(
      (params) => {
        this.datasetId = +params['id'];
        console.log(this.datasetId);
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

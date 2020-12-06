import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { File } from 'src/app/core/interface/file';
import { Similarity, SimilarityData } from 'src/app/core/interface/similarity';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.scss']
})
export class ResultComponent implements OnInit, OnDestroy {

  protected readonly unsubscribe$ = new Subject<void>();

  similarityId: number;
  similarity: Similarity;
  targets: File[];
  results: File[] = [];

  responsiveOptions: any[];

  constructor(
    private route: ActivatedRoute,
    private similaritiesServives: SimilarityData
  ) {

  }

  ngOnInit(): void {
    this.route.params.pipe(takeUntil(this.unsubscribe$)).subscribe(
      (params) => {
        this.similarityId = +params['id'];
        this.similaritiesServives.get(this.similarityId).pipe(takeUntil(this.unsubscribe$)).subscribe(
          (res) => {
            this.similarity = res;
            this.targets = this.similarity.targets;
            this.results = this.similarity.results;
            console.log(res);
          }
        )
      }
    )

    this.responsiveOptions = [
      {
        breakpoint: '1024px',
        numVisible: 3,
        numScroll: 3
      },
      {
        breakpoint: '768px',
        numVisible: 2,
        numScroll: 2
      },
      {
        breakpoint: '560px',
        numVisible: 1,
        numScroll: 1
      }
    ];

  }

  ngOnDestroy(): void {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

}

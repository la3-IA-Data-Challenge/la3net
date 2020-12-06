import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil, timeout } from 'rxjs/operators';
import { Similarity, SimilarityData } from 'src/app/core/interface/similarity';

@Component({
  selector: 'app-select-method',
  templateUrl: './select-method.component.html',
  styleUrls: ['./select-method.component.scss']
})
export class SelectMethodComponent implements OnInit, OnDestroy {

  protected readonly unsubscribe$ = new Subject<void>();

  similarityId: number;
  similarity: Similarity;

  // TODO : Rename methods - frontend
  methods: string[] = ["method1", "method2", "method3"];
  selectedMethod: string = this.methods[0];

  isLoading: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private similaritiesServives: SimilarityData,
    private router: Router,
  ) { }

  ngOnInit(): void {
    this.route.params.pipe(takeUntil(this.unsubscribe$)).subscribe(
      (params) => {
        this.similarityId = +params['id'];
      }
    )
  }

  execute(event): void {
    this.isLoading = true;

    let item: any = {
      similarityId: this.similarityId,
      method: this.selectedMethod,
    }

    this.similaritiesServives.execute(item).pipe(takeUntil(this.unsubscribe$)).subscribe(
      (res: Similarity) => {
        this.isLoading = false;
        this.similarity = res;
        this.router.navigate(['/result/', this.similarity.id]);
      }
    )
  }

  ngOnDestroy(): void {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

}

import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { SimilarityData } from 'src/app/core/interface/similarity';

@Component({
  selector: 'app-select-method',
  templateUrl: './select-method.component.html',
  styleUrls: ['./select-method.component.scss']
})
export class SelectMethodComponent implements OnInit, OnDestroy {

  protected readonly unsubscribe$ = new Subject<void>();

  similarityId: number;

  methods: string[] = ["method1", "method2", "method3"];
  selectedMethod: string = this.methods[0];

  constructor(
    private route: ActivatedRoute,
    private similaritiesServives: SimilarityData
  ) { }

  ngOnInit(): void {
    this.route.params.pipe(takeUntil(this.unsubscribe$)).subscribe(
      (params) => {
        this.similarityId = +params['id'];
      }
    )
  }

  execute(event): void {
    let item: any = {
      similarityId: this.similarityId,
      method: this.selectedMethod,
    }
    this.similaritiesServives.execute(item).pipe(takeUntil(this.unsubscribe$)).subscribe(
      (res) => {
        console.log(res);
      }
    )
  }

  ngOnDestroy(): void {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

}

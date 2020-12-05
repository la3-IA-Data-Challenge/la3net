import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { SimilarityRoutingModule } from './similarity-routing.module';
import { SelectOptionComponent } from './select-option/select-option.component';

import { ButtonModule } from 'primeng/button';
import { SelectTargetsComponent } from './select-targets/select-targets.component';


@NgModule({
  declarations: [SelectOptionComponent, SelectTargetsComponent],
  imports: [
    CommonModule,
    SimilarityRoutingModule,
    FormsModule,
    ReactiveFormsModule,

    // PRIME NG
    ButtonModule,
  ]
})
export class SimilarityModule { }

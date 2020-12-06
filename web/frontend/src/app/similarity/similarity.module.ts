import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { SimilarityRoutingModule } from './similarity-routing.module';
import { SelectOptionComponent } from './select-option/select-option.component';
import { SelectTargetsComponent } from './select-targets/select-targets.component';

import { ButtonModule } from 'primeng/button';
import { DragDropModule } from 'primeng/dragdrop';
import { ScrollPanelModule } from 'primeng/scrollpanel';
import { PaginatorModule } from 'primeng/paginator';
import { SelectMethodComponent } from './select-method/select-method.component';
import { RadioButtonModule } from 'primeng/radiobutton';


@NgModule({
  declarations: [SelectOptionComponent, SelectTargetsComponent, SelectMethodComponent],
  imports: [
    CommonModule,
    SimilarityRoutingModule,
    FormsModule,
    ReactiveFormsModule,

    // PRIME NG
    ButtonModule,
    DragDropModule,
    ScrollPanelModule,
    PaginatorModule,
    RadioButtonModule,
  ]
})
export class SimilarityModule { }

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NotFoundComponent } from '../not-found/not-found.component';
import { SelectOptionComponent } from './select-option/select-option.component';
import { SelectTargetsComponent } from './select-targets/select-targets.component';

const routes: Routes = [
  { path: 'step1', component: SelectOptionComponent },
  { path: 'step2/:id', component: SelectTargetsComponent },
  { path: '', redirectTo: 'step1', pathMatch: 'full' },
  { path: '', redirectTo: 'step1', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SimilarityRoutingModule { }

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectTargetsComponent } from './select-targets.component';

describe('SelectTargetsComponent', () => {
  let component: SelectTargetsComponent;
  let fixture: ComponentFixture<SelectTargetsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectTargetsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectTargetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

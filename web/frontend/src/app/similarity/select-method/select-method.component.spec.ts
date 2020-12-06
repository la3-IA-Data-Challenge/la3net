import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectMethodComponent } from './select-method.component';

describe('SelectMethodComponent', () => {
  let component: SelectMethodComponent;
  let fixture: ComponentFixture<SelectMethodComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectMethodComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectMethodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

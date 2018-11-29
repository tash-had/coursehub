import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RatingsCircleComponent } from './ratings-circle.component';

describe('RatingsCircleComponent', () => {
  let component: RatingsCircleComponent;
  let fixture: ComponentFixture<RatingsCircleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RatingsCircleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RatingsCircleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseReviewFormComponent } from './course-review-form.component';

describe('CourseReviewFormComponent', () => {
  let component: CourseReviewFormComponent;
  let fixture: ComponentFixture<CourseReviewFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CourseReviewFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CourseReviewFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

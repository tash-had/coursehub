import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursePrereqsComponent } from './course-prereqs.component';

describe('CoursePrereqsComponent', () => {
  let component: CoursePrereqsComponent;
  let fixture: ComponentFixture<CoursePrereqsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoursePrereqsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoursePrereqsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { TestBed } from '@angular/core/testing';

import { CourseReviewService } from './course-review.service';

describe('CourseReviewService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CourseReviewService = TestBed.get(CourseReviewService);
    expect(service).toBeTruthy();
  });
});

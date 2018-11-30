import { TestBed } from '@angular/core/testing';

import { CourseReviewServiceService } from './course-review-service.service';

describe('CourseReviewServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CourseReviewServiceService = TestBed.get(CourseReviewServiceService);
    expect(service).toBeTruthy();
  });
});

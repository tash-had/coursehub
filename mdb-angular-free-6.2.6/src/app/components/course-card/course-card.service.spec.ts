import { TestBed } from '@angular/core/testing';

import { CourseCardService } from './course-card.service';

describe('CourseCardService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CourseCardService = TestBed.get(CourseCardService);
    expect(service).toBeTruthy();
  });
});

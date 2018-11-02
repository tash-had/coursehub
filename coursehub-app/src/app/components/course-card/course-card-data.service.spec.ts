import { TestBed } from '@angular/core/testing';

import { CourseCardDataService } from './course-card-data.service';

describe('CourseCardDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CourseCardDataService = TestBed.get(CourseCardDataService);
    expect(service).toBeTruthy();
  });
});

import { TestBed } from '@angular/core/testing';

import { CoursePageDataService } from './course-page-data.service';

describe('CoursePageDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CoursePageDataService = TestBed.get(CoursePageDataService);
    expect(service).toBeTruthy();
  });
});

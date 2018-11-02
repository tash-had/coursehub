import { TestBed } from '@angular/core/testing';

import { CommentDataService } from './comment-data.service';

describe('CommentDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CommentDataService = TestBed.get(CommentDataService);
    expect(service).toBeTruthy();
  });
});

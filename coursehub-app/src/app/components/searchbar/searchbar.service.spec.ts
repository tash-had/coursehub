import { TestBed } from '@angular/core/testing';

import { SearchbarService } from './searchbar.service';

describe('SearchbarService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SearchbarService = TestBed.get(SearchbarService);
    expect(service).toBeTruthy();
  });
});

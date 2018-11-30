import { TestBed } from '@angular/core/testing';

import { UserProfileDataService } from './user-profile-data.service';

describe('UserProfileDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: UserProfileDataService = TestBed.get(UserProfileDataService);
    expect(service).toBeTruthy();
  });
});

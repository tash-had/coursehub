import { Component, Input } from '@angular/core';
import { UserProfileDataService } from '../../views/profile/user-profile-data.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent {
  @Input() userProfileData: object;
  constructor() { }
}

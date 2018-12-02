import { Component, OnInit, Input } from '@angular/core';
import { UserProfileDataService } from '../profile/user-profile-data.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  userProfileData: Object;

  constructor(private userProfileDataService: UserProfileDataService) { }

  ngOnInit() {
    this.userProfileDataService.getProfileData()
      .subscribe((data) => {
        this.userProfileData = data;
      });
  }

}

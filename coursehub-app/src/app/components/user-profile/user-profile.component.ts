import { Component, OnInit, Input } from '@angular/core';
import { UserProfileDataService } from './user-profile-data.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit {
  @Input() userProfileData: object;

  constructor(private userProfileDataService: UserProfileDataService) { }

  ngOnInit() {
    this.userProfileDataService.getProfileData("test")
      .subscribe((data) => {
        this.userProfileData = data;
      }
    );
  }
}

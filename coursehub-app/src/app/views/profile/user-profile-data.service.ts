import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserProfileDataService {
  userProfileDataUrlBase: string = 'https://coursehubapi.herokuapp.com/api/v1.0/user/view_user_profile';
  constructor(private http: HttpClient) { }

  getProfileData() {
    let idToken: string = localStorage.getItem("id_token");
    if (idToken && idToken.length > 0) {
      return this.http.get(this.userProfileDataUrlBase, {
        "headers": new HttpHeaders({
          "Content-Type": "application/json",
          "Authorization": localStorage.getItem("id_token")
        })
      });
    }
  }
}


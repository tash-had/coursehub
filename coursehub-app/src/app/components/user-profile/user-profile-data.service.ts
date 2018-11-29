import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserProfileDataService {
  userProfileDataUrlBase : string = 'http://localhost:5000/api/v1.0/user/view_user_profile';
  constructor(private http: HttpClient) { }
  
  getProfileData(userId: String) {
    return this.http.get(this.userProfileDataUrlBase, {
      "headers": new HttpHeaders({
        "Content-Type": "application/json",
        "Authorization": localStorage.getItem("id_token")
      })
    });  
  }
}


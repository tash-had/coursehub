import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserProfileDataService {
  courseDataUrlBase : string = 'https://coursehubapi.herokuapp.com/api/v1.0/course/get_course_data?courseId=';
  constructor(private http: HttpClient) { }

  getProfileData(userId: String) {
    return this.http.get(this.courseDataUrlBase + courseId.toString());
  }
}

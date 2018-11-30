import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoursePageDataService {
  courseDataUrlBase : string = 'http://0.0.0.0:5000/api/v1.0/course/get_course_data?courseId=';
  constructor(private http: HttpClient) { }

  getCourseData(courseId: String) {
    return this.http.get(this.courseDataUrlBase + courseId.toString());
  }
}

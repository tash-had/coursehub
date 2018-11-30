import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CourseReviewServiceService {
  courseReviewUrlBase = 'https://coursehubapi.herokuapp.com/api/v1.0/course/search_course?searchQuery=';

  constructor(private http: HttpClient) { }
  
  reviewCourse(workloadRating: number, recommendationRating: number, courseId: number, userId: number) {
    return this.http.put(this.courseReviewUrlBase, {
      "workloadRating": workloadRating,
      "recommendationRating": recommendationRating,
      "courseId": courseId,
      "userId": userId
    });
  }
}

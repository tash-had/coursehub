import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CourseReviewService {
  courseReviewUrlBase = 'http://127.0.0.1:5000/api/v1.0/course';

  constructor(private http: HttpClient) { }
  
  reviewCourse(difficultyRating: number, usefulnessRating: number, courseId: number) {
    let rateCourseEndpoint = "/add_course_ratings";
    return this.http.put(this.courseReviewUrlBase + rateCourseEndpoint, {
      "workloadRating": difficultyRating,
      "recommendationRating": usefulnessRating,
      "courseId": courseId
    });
  }
}

import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

@Injectable()
export class CourseCardDataService {

  private courseCodeDataSource = new BehaviorSubject('Course');
  private courseDescriptionDataSource = new BehaviorSubject('Course Description');
  private courseTotalRatingDataSource = new BehaviorSubject(0);

  courseCode = this.courseCodeDataSource.asObservable();
  courseDescription = this.courseDescriptionDataSource.asObservable();
  courseTotalRating = this.courseTotalRatingDataSource.asObservable();

  constructor() { }

  populateCourseCardData(courseCode: string, courseDescription: string, courseTotalRating: number) {
    this.courseCodeDataSource.next(courseCode);
    this.courseDescriptionDataSource.next(courseDescription);
    this.courseTotalRatingDataSource.next(courseTotalRating);
  }
}
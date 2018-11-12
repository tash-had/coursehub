import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

@Injectable()
export class CourseCardDataService {

  private courseDataSource = new BehaviorSubject({});

  courseData = this.courseDataSource.asObservable();

  constructor() { }

  setCourseCardData(courseData: Object) {
    this.courseDataSource.next(courseData);
  }
}
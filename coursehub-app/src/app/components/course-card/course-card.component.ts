import { Component, Input} from '@angular/core';
import { CourseCardDataService } from "./course-card-data.service";
import { Router } from '@angular/router';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss'],
})

export class CourseCardComponent {
  @Input() courseData : Object;
  @Input() color: String;
  @Input() percentColor: String;
  Math: any;

  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;

  constructor(private courseCardDataService: CourseCardDataService, private _router: Router) {
    this.color = 'blue';
    this.Math = Math;
  }

  getOverallRatingAsPercent() {
    return this.Math.round(100*(this.courseData['course_overall_rating']/5));
  }

  navigateToCoursePage() {
    this._router.navigate(['/course/']);
    this.courseCardDataService.setCourseCardData(this.courseData);
  }
}

import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { CourseCardService } from './course-card.service';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss'],
})
export class CourseCardComponent implements OnInit {
  @Input() name : String = 'CSC165H1';
  @Input() description: String;
  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;
  totalRating: number;


  constructor(private courseCardService: CourseCardService) {
    this.totalRating = 86;
  }

  ngOnInit() {
    this.courseCardService.getCourse(this.name)
    .subscribe((data) => this.description = data['courseData']['courseDescription']);
  }



}

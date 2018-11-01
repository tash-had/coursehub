import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss'],
})
export class CourseCardComponent {
  @Input() name : String = '';
  @Input() description: String;
  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;
  totalRating: number;

  constructor() {
    this.totalRating = 86;
  }



}

import { Component,Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss'],
})
export class CourseCardComponent {
  @Input() name : String = '';
  @Input() description: String;
  @Input() color: String;
  @Input() percentColor: String;
  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;
  totalRating: number;

  constructor() {
    this.totalRating = 86;
    this.color = 'blue';
    this.percentColor='orange';
  }


}

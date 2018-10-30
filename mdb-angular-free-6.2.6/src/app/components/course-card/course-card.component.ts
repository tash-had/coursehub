import { Component, OnInit } from '@angular/core';
import { CourseCardService } from './course-card.service';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss']
})
export class CourseCardComponent implements OnInit {
  name : String = 'CSC165H1';
  description: String;
  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;
  comments: String[] = [];
  currentComment: String;

  constructor(private courseCardService: CourseCardService) {
    
  }

  ngOnInit() {
    this.courseCardService.getCourse(this.name)
    .subscribe((data) => this.description = data['courseData']['courseDescription']);
  }

  addComment() {
    if (this.currentComment){
      if (this.currentComment.trim()){
        this.comments.push(this.currentComment);
        this.currentComment = null;
       
      }
    }
  }

}

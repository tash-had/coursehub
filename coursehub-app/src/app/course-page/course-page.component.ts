import { Component, OnInit } from '@angular/core';
import { CourseCardDataService } from '../components/course-card/course-card-data.service'

@Component({
  selector: 'app-course-page',
  templateUrl: './course-page.component.html',
  styleUrls: ['./course-page.component.scss']
})

export class CoursePageComponent implements OnInit {
  courseData: Object;

  //mock comments
  comments: String[] = ['Hey, I love CSC301', 'Hey, I do not like CSC301 that much', 
  'Why does no one shower??', 'I failed my assignment, can I drop this course?', "Why don't we just use reddit"];
  currentComment: String;
  constructor(private courseCardDataService: CourseCardDataService) {}

  ngOnInit() {
    this.courseCardDataService.courseData.subscribe(courseData => this.courseData = courseData)
  }

  addComment() {
    if (this.currentComment && this.currentComment.trim()){
        this.comments.push(this.currentComment);
        this.currentComment = null;       
    }
  }
}

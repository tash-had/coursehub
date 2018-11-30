import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  courseData: Object;

  //mock comments
  comments: String[] = ['Hey, I love CSC301', 'Hey, I do not like CSC301 that much', 
  'Why does no one shower??', 'I failed my assignment, can I drop this course?', "Why don't we just use reddit"];
  currentComment: String;
  constructor() {}

  ngOnInit() {
    
  }

  addComment() {
    if (this.currentComment && this.currentComment.trim()){
        this.comments.push(this.currentComment);
        this.currentComment = null;       
    }
  }

}

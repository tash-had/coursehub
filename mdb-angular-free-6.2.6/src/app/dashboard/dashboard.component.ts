import { Component, OnInit, } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  comments: String[] = [];
  currentComment: String;
  courseSearch:Object;


  constructor() {}
  
  ngOnInit() {

  }
  receiveMessage($event) {
    console.log($event)
    this.courseSearch = $event
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

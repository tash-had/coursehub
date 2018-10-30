import { Component, OnInit } from '@angular/core';
import {DashboardService} from './dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  name : String = 'CSC165';
  description: String;
  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;
  comments: String[] = [];
  currentComment: String;

  constructor(private dashboardService: DashboardService) {
    
  }

  ngOnInit() {
    this.dashboardService.getCourse(this.name+'H1')
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

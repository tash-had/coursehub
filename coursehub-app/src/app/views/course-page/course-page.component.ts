import { Component, OnInit,  ElementRef, ViewChild } from '@angular/core';
import { CourseCardDataService } from '../../components/course-card/course-card-data.service'
import { ActivatedRoute } from '@angular/router';
import { CoursePageDataService } from './course-page-data.service'

@Component({
  selector: 'app-course-page',
  templateUrl: './course-page.component.html',
  styleUrls: ['./course-page.component.scss']
})

export class CoursePageComponent implements OnInit {
  courseData: Object;
  usefulCourseRating: number;
  difficultCourseRating: number;
  ratingsExist: boolean = true;
  comments: String[] = [];
  currentComment: String;
  constructor(private courseCardDataService: CourseCardDataService, private coursePageDataService: CoursePageDataService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.courseCardDataService.courseData.subscribe(courseData => this.courseCardDataReceived(courseData));
    this.checkForRatings();
    this.initializeRatings();

  }

  courseCardDataReceived(courseData: Object) {
    if (courseData && courseData.hasOwnProperty("id_")) {
      this.courseData = courseData;
    } else {
      this.getCourseData(); 
    }
  }

  checkForRatings(){
    if (this.courseData){
      if (this.courseData['rating_count'] == 0){
        this.ratingsExist = false;
      }
    }
  }

  initializeRatings(){
    if (this.courseData){
      this.difficultCourseRating = Math.round(100*(this.courseData['ratings']['workload_rating']/5));
      this.usefulCourseRating = Math.round(100*(this.courseData['ratings']['recommendation_rating']/5));
    }
    
  
  }
  setRatings(type:string) : number {
    if (this.courseData){
      if (type == 'useful'){
        return this.usefulCourseRating;
      }
      else {
        return this.difficultCourseRating;
      }
    }

  }

  getCourseData() {
    const courseId = +this.route.snapshot.paramMap.get('courseId');
    this.coursePageDataService.getCourseData(courseId.toString())
      .subscribe((courseData) => {
        this.courseData = courseData;
        this.checkForRatings();
        this.initializeRatings();
      });
  }

  addComment() {
    if (this.currentComment && this.currentComment.trim()){
        this.comments.push(this.currentComment);
        this.currentComment = null;       
    }
  }
}

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
  @ViewChild("useRating") usefulRating: ElementRef;
  @ViewChild("usefulnessSlider") usefulSlider: ElementRef;
  @ViewChild("diffRating") diffRating: ElementRef;
  @ViewChild("difficultySlider") difficultSlider: ElementRef;
  @ViewChild("slidersForm") slidersForm: ElementRef;
  
  usefulCourseRating: number;
  difficultCourseRating: number;
  ratingsExist: boolean = true;

  //mock comments
  comments: String[] = ['Hey, I love CSC301', 'Hey, I do not like CSC301 that much', 
  'Why does no one shower??', 'I failed my assignment, can I drop this course?', "Why don't we just use reddit"];
  currentComment: String;
  constructor(private courseCardDataService: CourseCardDataService, private coursePageDataService: CoursePageDataService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.courseCardDataService.courseData.subscribe(courseData => this.courseCardDataReceived(courseData));
    this.setSliders();

  }

  courseCardDataReceived(courseData: Object) {
    if (courseData && courseData.hasOwnProperty("id_")) {
      this.courseData = courseData;
    } else {
      this.getCourseData(); 
    }
  }

  setSliders(){
    if (this.courseData){
      if (this.courseData['rating_count'] == 0){
        this.ratingsExist = false;
        this.slidersForm.nativeElement.empty();
      }
      else{
    this.usefulCourseRating = this.courseData['ratings']['recommendation_rating'];
    this.difficultCourseRating = this.courseData['ratings']['workload_rating'];
      }

    }

    this.usefulSlider.nativeElement.value = Math.round(100*(this.usefulCourseRating / 5));
    this.usefulRating.nativeElement.innerHTML = Math.round(100*(this.usefulCourseRating / 5));
    this.difficultSlider.nativeElement.value = Math.round(100*(this.difficultCourseRating / 5));
    this.diffRating.nativeElement.innerHTML = Math.round(100*(this.difficultCourseRating / 5));
  }

  getCourseData() {
    const courseId = +this.route.snapshot.paramMap.get('courseId');
    this.coursePageDataService.getCourseData(courseId.toString())
      .subscribe((courseData) => {
        this.courseData = courseData;
        this.setSliders();
      });
  }

  addComment() {
    if (this.currentComment && this.currentComment.trim()){
        this.comments.push(this.currentComment);
        this.currentComment = null;       
    }
  }

  updateRating(type: String){
    if (type == 'usefulness'){
      this.usefulRating.nativeElement.innerHTML = this.usefulSlider.nativeElement.value;
    }else if (type == 'difficulty'){
      this.diffRating.nativeElement.innerHTML = this.difficultSlider.nativeElement.value;
    }
    
  }

  assignRatingLevel(type: string) : string {
    if (type == 'usefulness'){
      var usefulNum = Math.round(100*(this.usefulCourseRating / 5));
      if (usefulNum > 79){
        return 'green';
      }
      else if (usefulNum <= 79 && usefulNum > 59){
        return 'yellow';
      }
      else{
        return 'red';
      }
    }
    else if (type == 'difficulty'){
      var difficultNum = Math.round(100*(this.difficultCourseRating / 5));
      if (difficultNum > 79){
        return 'green';
        
      }
      else if (difficultNum <= 79 && difficultNum > 59){
        return 'yellow';
      }
      else{
        return 'red';
      }
    }
  } 
}

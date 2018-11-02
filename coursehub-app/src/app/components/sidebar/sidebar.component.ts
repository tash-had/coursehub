import { Component, OnInit } from '@angular/core';
import { CourseCardDataService } from '../course-card/course-card-data.service'

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  courseCode: String;
  courseDescription: String;
  courseOverallRating: number;

  constructor(private courseCardDataService: CourseCardDataService) { }

  ngOnInit() {
    this.courseCardDataService.courseCode.subscribe(courseCode => this.courseCode = courseCode)
    this.courseCardDataService.courseDescription.subscribe(courseDescription => this.courseDescription = courseDescription)
    this.courseCardDataService.courseOverallRating.subscribe(courseOverallRating => this.courseOverallRating = courseOverallRating)
  }

}

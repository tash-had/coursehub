import { Component, OnInit } from '@angular/core';
import {SearchbarService} from './searchbar.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.scss']
})
export class SearchbarComponent implements OnInit {
  COURSE_MATCHER = new RegExp("^[a-zA-Z]{3}[0-9]{1,3}$");
  
  course : string;
  coursePreview: Object;
  
  constructor(private searchbarService: SearchbarService) { }

  ngOnInit() {
  }

  checkValidInput(event: any) : boolean{
    if (this.course && this.course.length > 3  && this.COURSE_MATCHER.test(this.course)){
      this.searchbarService.getCourses(this.course)
      .subscribe((data) => this.coursePreview = data
      );
    }

    return true;
  }

}

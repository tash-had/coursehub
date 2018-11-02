import { Component, OnInit, Output ,  EventEmitter} from '@angular/core';
import {SearchbarService} from './searchbar.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.scss']
})
export class SearchbarComponent implements OnInit {
  COURSE_MATCHER = new RegExp("^[a-zA-Z]{3}[0-9]{1,3}$");
  course : string;
  themeUpdated : boolean = false;
  @Output() messageEvent = new EventEmitter<Object>();
  
  constructor(private searchbarService: SearchbarService) { }

  ngOnInit() {
  }

  checkValidInput(event: any) : void{
    let inputWasAlphanumeric = /[a-zA-Z0-9-_ ]/.test(String.fromCharCode(event.keyCode));
    if (this.course && (inputWasAlphanumeric && this.course && this.course.length > 3 && this.COURSE_MATCHER.test(this.course)) || this.course.length == 0){
      if (this.course === "CSC69") {
        this.messageEvent.emit("update theme - black");
      } else {
        this.messageEvent.emit("update theme - blue")
      }
      this.searchbarService.getCourses(this.course)
        .subscribe((data) => this.messageEvent.emit(data)
      );
    }
    
    
  }

}

import { Component, OnInit, AfterViewInit, Output ,  EventEmitter} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {SearchbarService} from './searchbar.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.scss']
})
export class SearchbarComponent implements OnInit {
  course : string;
  themeUpdated : boolean = false;
  @Output() messageEvent = new EventEmitter<Object>();
  
  constructor(private searchbarService: SearchbarService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.setSearchQueryFromUrlParam();
   
  }

  ngAfterViewInit(): void {
  }

  checkValidInput(input: string, keyCode=-1) : boolean{
    let inputWasAlphanumeric = /[a-zA-Z0-9-]/.test(input);
    if ((inputWasAlphanumeric && this.course && this.searchbarService.COURSE_MATCHER.test(this.course)) || keyCode === 8){
      return true;
    }
    return false;
  }

  fetchSearchResults(event: any) : void{
    if (this.checkValidInput(String.fromCharCode(event.keyCode)), event.keyCode) {
      if (this.course === "CSC69") {
        this.messageEvent.emit("update theme - black");
      } else {
        this.messageEvent.emit("update theme - blue")
      }
      this.sendRequest();
    }
  }

  sendRequest() {
    this.messageEvent.emit(this.course);
    this.searchbarService.getCourses(this.course)
      .subscribe((data) => this.messageEvent.emit(data)
    );
  }

  setSearchQueryFromUrlParam() {
    this.course = this.route.snapshot.paramMap.get('searchQuery');   
    if (this.checkValidInput(this.course)) {
      this.sendRequest();
    } else {
      this.course = null;
    }
  }
}

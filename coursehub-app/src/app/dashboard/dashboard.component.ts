import { Component, AfterViewInit, ElementRef, ViewChild, } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements AfterViewInit {
  comments: String[] = [];
  currentComment: String;
  courseSearchResponse: Object;
  @ViewChild('coursehubLogo') coursehubLogo; 

  constructor(private elementRef: ElementRef) {}

  ngAfterViewInit(): void {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'black';
  }

  receiveMessage($event) {
    if (typeof($event) === "string" && $event === "update theme") {
      this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'white';
      this.coursehubLogo.nativeElement.src = "../../assets/Courshub-blue.png";
    } else {
      this.courseSearchResponse = $event
    }
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

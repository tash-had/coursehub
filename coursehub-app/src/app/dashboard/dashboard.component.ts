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
    this.toggleTheme(true)
  }

  receiveMessage($event) {
    if (typeof($event) === "string") {
      if ($event === "update theme - blue") {
        this.toggleTheme(true);
      } else if ($event === "update theme - black") {
        this.toggleTheme(false);
      }
    } else {
      this.courseSearchResponse = $event
    }
  }

  toggleTheme(blueTheme: boolean) {
    if (blueTheme) {
      this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'white';
      this.coursehubLogo.nativeElement.src = "../../assets/Courshub-blue.png";
    } else {
      this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'black';
      this.coursehubLogo.nativeElement.src = "../../assets/Courshub.png";
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

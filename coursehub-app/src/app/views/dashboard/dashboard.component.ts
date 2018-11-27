import { Component, AfterViewInit, ElementRef, ViewChild, OnInit} from '@angular/core';
import { SearchbarService } from '../../components/searchbar/searchbar.service';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements AfterViewInit {
  comments: String[] = [];
  currentComment: String;
  courseSearchResponse: Object;
  searchQuery: string;
  
  @ViewChild('coursehubLogo') coursehubLogo; 
  
  constructor(private elementRef: ElementRef, private searchService: SearchbarService, private _router : Router, public auth: AuthService) {
  }
  ngOnInit() {
  }

  ngAfterViewInit(): void {
    this.toggleTheme(true);
    this.searchQuery = this.searchService.lastSearchQuery;
  }

  receiveMessage($event) {
    if (typeof($event) === "string") {
      if ($event === "update theme - blue") {
        this.toggleTheme(true);
      } else if ($event === "update theme - black") {
        this.toggleTheme(false);
      } else {
        // searchQuery was passed in
        this.searchQuery = $event;
      }
    } else {
      this.courseSearchResponse = $event
    }
  }

  toggleTheme(blueTheme: boolean) {
    if (blueTheme) {
      this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'white';
      this.coursehubLogo.nativeElement.src = "https://coursehub.ca/assets/Courshub-blue.png";
    } else {
      this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'black';
      this.coursehubLogo.nativeElement.src = "https://coursehub.ca/assets/Courshub.png";
    }
  }

  navigateHome() {
    location.reload();
  }
}

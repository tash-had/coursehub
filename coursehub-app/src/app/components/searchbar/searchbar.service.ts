import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SearchbarService {
  courseUrl = 'https://coursehubapi.herokuapp.com/api/v1.0/course/search_course?searchQuery=';
  public lastSearchQuery: string;
  public COURSE_MATCHER = new RegExp("^[a-zA-Z]{3}[0-9]{1,3}$");
  public searchResults: object = {};

  constructor(private http: HttpClient) { }
  
  getCourses(searchQuery: string) {
    if (searchQuery.length > 0) {
      this.lastSearchQuery = searchQuery;
      return this.http.get(this.courseUrl + searchQuery);
    }
    return of([]);
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SearchbarService {
  courseUrl = 'http://127.0.0.1:5000/api/v1.0/search_course?searchQuery=';;
  constructor(private http: HttpClient) { }

  getCourses(course: String) {
    return this.http.get(this.courseUrl + course);
  }
}

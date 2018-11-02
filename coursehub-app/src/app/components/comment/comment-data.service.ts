import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CommentDataService {

  commentUrl : string;
  constructor(private http: HttpClient) { }

  getComments(course: String) {
    return this.http.get(this.commentUrl + course);
  }

}

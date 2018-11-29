import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CommentDataService {

  commentUrl : string = 'https://coursehubapi.herokuapp.com/api/v1.0/comment/get_comments?courseId=';
  constructor(private http: HttpClient) { }

  getComments(course: String) {
    return this.http.get(this.commentUrl + course);
  }
}

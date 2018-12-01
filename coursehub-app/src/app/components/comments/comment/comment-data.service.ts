import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CommentDataService {

  commentUrlBase : string = 'https://coursehubapi.herokuapp.com/api/v1.0/comment';
  constructor(private http: HttpClient) { }

  getComments(courseId: String) {
    let getCommentsEndpoint = "/get_comments?courseId=";
    return this.http.get(this.commentUrlBase + getCommentsEndpoint + courseId);
  }

  postComment(commentText: String, courseId: number, parentId: string) {
    let postCommentEndpoint = "/post_comment";
    return this.http.post(this.commentUrlBase + postCommentEndpoint, {
      "commentText": commentText,
      "courseId": courseId,
      "parentId": parentId
    });
  }
}

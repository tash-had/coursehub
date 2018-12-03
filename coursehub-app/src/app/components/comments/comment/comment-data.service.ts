import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CommentDataService {

  commentUrlBase : string = 'http://0.0.0.0:5000/api/v1.0/comment';
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

  upvoteCourse(commentId: number) {
    let upvoteEndpoint = "/upvote";
    return this.http.put(this.commentUrlBase + upvoteEndpoint, {
      "commentId": commentId
    });  
  }
  
  downvoteCourse(commentId: number) {
    let downvoteEndpoint = "/downvote";
    return this.http.put(this.commentUrlBase + downvoteEndpoint, {
      "commentId": commentId
    });  
  }

}

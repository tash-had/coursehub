import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})

export class CommentComponent implements OnInit {
  @Input() comments: String[] = [];
  // currentComment: String;
  constructor() {
  	console.log("COMMENT");
  	console.log(this.comments);
  }

  ngOnInit() {}

  // addComment() {
  //   if (this.currentComment){
  //     if (this.currentComment.trim()){
  //       this.comments.push(this.currentComment);
  //       this.currentComment = null;
       
  //     }
  //   }
  // }
}
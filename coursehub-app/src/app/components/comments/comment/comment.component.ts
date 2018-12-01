import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import {CommentDataService} from './comment-data.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss'],
  encapsulation: ViewEncapsulation.None
})

export class CommentComponent implements OnInit {
  @Input() comment: Object;

  constructor(private commentService: CommentDataService) {
  }

  hasReplies(): boolean {
    return this.comment['replies'].length > 0;
  }

  ngOnInit() {
  }

  upvoteComment(){
    this.comment['score']++;
    this.commentService.upvoteCourse(this.comment['comment_id']);

  }

  downvoteComment(){
    this.comment['score']--;
    this.commentService.downvoteCourse(this.comment['comment_id']);
  }
}
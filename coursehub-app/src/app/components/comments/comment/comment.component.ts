import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import {CommentDataService} from './comment-data.service';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss'],
  encapsulation: ViewEncapsulation.None
})

export class CommentComponent implements OnInit {
  @Input() comment: Object;

  constructor(private commentService: CommentDataService, public authService: AuthService) {
  }

  hasReplies(): boolean {
    return this.comment['replies'].length > 0;
  }

  ngOnInit() {
  }

  upvoteComment(){
    if (this.authService.isAuthenticated()) {
      this.comment['score'] = this.comment['score'] + 1;
      this.commentService.upvoteCourse(this.comment['comment_id']).subscribe(() => {});
    } else {
      alert("You must login to vote!");
    }
  }

  downvoteComment(){
    if (this.authService.isAuthenticated()) {
      this.comment['score'] = this.comment['score'] - 1;
      this.commentService.downvoteCourse(this.comment['comment_id']).subscribe(() => {});
    } else {
      alert("You must login to vote!");
    }
  }
}
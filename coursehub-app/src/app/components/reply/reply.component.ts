import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { CommentDataService } from '../comments/comment/comment-data.service';

@Component({
  selector: 'app-reply',
  templateUrl: './reply.component.html',
  styleUrls: ['./reply.component.scss']
})
export class ReplyComponent implements OnInit {
  replyInput: string = "";
  @Input() comment: object;
  @ViewChild('content') public contentModal;

  
  constructor(private commentService: CommentDataService) { }

  ngOnInit() {
  }

  showReplyModal(){
    this.contentModal.show();
  }

  ratingHTMLStartIndex() {
    return this.comment['text'].indexOf("<br>");
  }

  sendReply() {
    if (this.replyInput.trim().length > 0) {
      this.commentService.postComment(this.replyInput.trim(), this.comment['course_id'], this.comment['comment_id']).subscribe((res) => {
        this.contentModal.hide();
      });
    }
  }

  
}

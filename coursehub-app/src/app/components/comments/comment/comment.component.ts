import { Component, OnInit, Input } from '@angular/core';
import {CommentDataService} from './comment-data.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})

export class CommentComponent implements OnInit {
  @Input() comment: Object;

  constructor() {
  }

  hasReplies(): boolean {
    console.log(this.comment['replies'])
    return this.comment['replies'].length > 0;
  }

  ngOnInit() {
    // this.commentService.getComments(this.courseId.toString())
      // .subscribe((data) => this.parseData(data)
    // );
  }

  // parseData(data: Object) : void{
  //   for (let comment in data['comments']){
  //     this.comments.push(comment['text']);
  //   }
  // }
}
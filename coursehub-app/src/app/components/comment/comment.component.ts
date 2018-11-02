import { Component, OnInit, Input } from '@angular/core';
import {CommentDataService} from './comment-data.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})

export class CommentComponent implements OnInit {
  @Input() comments: String[] = [];
  @Input() course: string;
  constructor(private commentService: CommentDataService) {
  }

  ngOnInit() {
    // this.commentService.getComments(this.course)
    // .subscribe((data) => this.comments = data
    // );
  }
}
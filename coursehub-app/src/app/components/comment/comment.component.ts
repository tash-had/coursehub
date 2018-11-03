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
  @Input() courseId: number;
  constructor(private commentService: CommentDataService) {
  }

  ngOnInit() {
    this.commentService.getComments(this.courseId.toString())
    .subscribe((data) => this.comments = this.parseData(data)
    );
  }

  parseData(data: Object) : String[] {
    for (let comment in data['comments']){
      this.comments.push(comment['text']);
    }
    return []
  }
}
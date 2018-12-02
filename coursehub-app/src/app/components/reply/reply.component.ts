import { Component, OnInit, Input, ViewChild } from '@angular/core';

@Component({
  selector: 'app-reply',
  templateUrl: './reply.component.html',
  styleUrls: ['./reply.component.scss']
})
export class ReplyComponent implements OnInit {
  @Input() comment: object;
  @ViewChild('content') public contentModal;

  
  constructor() { }

  ngOnInit() {
  }

  showReplyModal(){
    this.contentModal.show();
  }
  
}

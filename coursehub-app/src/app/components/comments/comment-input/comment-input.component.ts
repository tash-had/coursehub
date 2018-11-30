import { Component, OnInit, Input } from '@angular/core';
type textSubmissionCallback = (submission: string) => any;

@Component({
  selector: 'app-comment-input',
  templateUrl: './comment-input.component.html',
  styleUrls: ['./comment-input.component.scss']
})
export class CommentInputComponent implements OnInit {
  @Input() inputLabel: string = "Write something ...";
  @Input() submitBtn: boolean = true;
  @Input() textSubmissionCallback: textSubmissionCallback;
  @Input() inputText: string = "";

  constructor() { }

  ngOnInit() {
  }

  onTextEntered(triggeredByBtn : boolean) : void {
    if (triggeredByBtn && this.submitBtn || !triggeredByBtn && !this.submitBtn) {
      this.textSubmissionCallback(this.inputText);
    }
  }
}

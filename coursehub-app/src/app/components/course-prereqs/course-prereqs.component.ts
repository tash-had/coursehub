import { Component, OnInit ,  ViewChild, ElementRef, Input} from '@angular/core';

@Component({
  selector: 'app-course-prereqs',
  templateUrl: './course-prereqs.component.html',
  styleUrls: ['./course-prereqs.component.scss']
})
export class CoursePrereqsComponent implements OnInit {
  @ViewChild('prereqElement') prereq: ElementRef;
  @ViewChild('coreqElement') coreq: ElementRef;
  @ViewChild('excluElement') exclu: ElementRef;
  @ViewChild('breadthElement') breadth: ElementRef;
  @Input() prereqIn: string = '';
  @Input() coreqIn : string = '';
  @Input() excluIn : string = '';
  @Input() breadthIn : string = '';

  constructor() { }

  ngOnInit() {

  }

  ngOnChanges() {
    if (this.prereqIn == ''){
      this.prereq.nativeElement.innerHTML = ' None'
    }
    else{
      this.prereq.nativeElement.innerHTML = ' ' + this.prereqIn;
    }

    if (this.coreqIn == ''){
      this.coreq.nativeElement.innerHTML = ' None'
    }
    else{
      this.coreq.nativeElement.innerHTML = ' ' + this.coreqIn;
    }

    if (this.excluIn == ''){
      this.exclu.nativeElement.innerHTML = ' None'
    }
    else{
      this.exclu.nativeElement.innerHTML = ' ' + this.excluIn;
    }

    if (this.breadthIn == ''){
      this.breadth.nativeElement.innerHTML = ' None'
    }
    else{
      this.breadth.nativeElement.innerHTML = ' ' +this.breadthIn;
    }
    
  }

}

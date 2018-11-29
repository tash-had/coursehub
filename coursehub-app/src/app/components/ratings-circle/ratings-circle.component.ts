import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-ratings-circle',
  templateUrl: './ratings-circle.component.html',
  styleUrls: ['./ratings-circle.component.scss']
})
export class RatingsCircleComponent implements OnInit {
  @Input() rating: number = 50;
  @Input() hide: boolean = false;
  @Input() percentColor: string = 'orange';

  constructor() { }

  ngOnInit() {
  }

}

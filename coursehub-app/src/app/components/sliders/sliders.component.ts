import { Component, OnInit, ViewChild, ElementRef, Input} from '@angular/core';

@Component({
  selector: 'app-sliders',
  templateUrl: './sliders.component.html',
  styleUrls: ['./sliders.component.scss']
})
export class SlidersComponent implements OnInit {

  @ViewChild('ratingSlider') ratingSlider: ElementRef;
  @ViewChild('numRating') rating: ElementRef;
  @Input() initialRating: number = 50;
  @Input() sliderDisabled = false;
  @Input() label : string;
  constructor() { }

  ngOnInit() {
    this.rating.nativeElement.innerHTML = this.initialRating;
    this.ratingSlider.nativeElement.value = this.initialRating;
  }

  updateRating(){
    this.rating.nativeElement.innerHTML = this.ratingSlider.nativeElement.value;
  }

  assignRatingLevel() : string {
    if (this.ratingSlider.nativeElement.value > 79){
      return 'high';
    }
    else if (this.ratingSlider.nativeElement.value <= 79 && this.ratingSlider.nativeElement.value > 59){
      return 'medium';
    }
    else{
      return 'low';
    }
  }

}

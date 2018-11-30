import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import { CourseReviewService } from './course-review.service';
import { CommentDataService } from '../comments/comment/comment-data.service';

@Component({
  selector: 'app-course-review-form',
  templateUrl: './course-review-form.component.html',
  styleUrls: ['./course-review-form.component.scss']
})
export class CourseReviewFormComponent implements OnInit {
  @Input() courseData: object;
  @ViewChild('usefulnessRatingSlider') usefulnessRatingSlider: ElementRef;
  @ViewChild('difficultyRatingSlider') difficultyRatingSlider: ElementRef;
  @ViewChild('optionalCommentText') optionalCommentInput: ElementRef;

  constructor(private courseReviewService: CourseReviewService, private commentDataService: CommentDataService) { }

  ngOnInit() {
  }

  submitReview() {
    let rawUsefulnessRating = this.usefulnessRatingSlider['ratingSlider'].nativeElement.value;
    let rawDifficultyRating = this.difficultyRatingSlider['ratingSlider'].nativeElement.value;
    let usefulnessRating: number = 5 * (rawUsefulnessRating/100);
    let difficultyRating: number = 5 * (rawDifficultyRating/100);
    let optionalComment: string = this.optionalCommentInput['inputText'];
        
    let usefulnessRatingStr = "<br><div class='inCommentRatingsContainer'><span class='inCommentRating'>" + rawUsefulnessRating +"</span><br>";
    let difficultyRatingStr = "<span class='inCommentRating'>" + rawDifficultyRating +"</span></div>";
    let commentWithRatings = optionalComment.concat(usefulnessRatingStr, difficultyRatingStr);

    this.commentDataService.postComment(commentWithRatings, this.courseData['id_'], null).subscribe(() => {
      
    });

    this.courseReviewService.reviewCourse(difficultyRating, usefulnessRating, this.courseData['id_']).subscribe(() => {});

  }
}

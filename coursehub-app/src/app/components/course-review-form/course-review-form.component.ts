import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import { CourseReviewService } from './course-review.service';
import { CommentDataService } from '../comments/comment/comment-data.service';
import { AuthService } from 'src/app/auth/auth.service';
import { ModalDirective } from 'angular-bootstrap-md';
import { Router, ActivatedRoute } from '@angular/router';

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
  @ViewChild('courseReviewFormModal') courseReviewFormModal: ModalDirective;

  constructor(private courseReviewService: CourseReviewService, private commentDataService: CommentDataService, public authService: AuthService, private router: Router, private route: ActivatedRoute) { }

  ngOnInit() {
  }

  submitReview() {
    let rawUsefulnessRating = this.usefulnessRatingSlider['ratingSlider'].nativeElement.value;
    let rawDifficultyRating = this.difficultyRatingSlider['ratingSlider'].nativeElement.value;
    let usefulnessRating: number = 5 * (rawUsefulnessRating / 100);
    let difficultyRating: number = 5 * (rawDifficultyRating / 100);
    let optionalComment: string = this.optionalCommentInput['inputText'];

    let usefulnessRatingStr = "<div class='inCommentRatingsContainer'><span class='inCommentRatingLabel'>Usefulness:</span> <span class='inCommentRating'>" + rawUsefulnessRating + "</span><br>";
    let difficultyRatingStr = "<span class='inCommentRatingLabel'>Difficulty:</span> <span class='inCommentRating'>" + rawDifficultyRating + "</span></div>";
    if (optionalComment.length > 0) {
      optionalComment = optionalComment.concat("<br>", usefulnessRatingStr, difficultyRatingStr);
    } else {
      optionalComment = optionalComment.concat(usefulnessRatingStr, difficultyRatingStr);
    }

    this.commentDataService.postComment(optionalComment, this.courseData['id_'], null).subscribe(() => { });

    this.courseReviewService.reviewCourse(difficultyRating, usefulnessRating, this.courseData['id_']).subscribe(() => { });
    this.courseReviewFormModal.hide();

    const courseId = +this.route.snapshot.paramMap.get('courseId');

    if (this.courseData['rating_count'] == 0) {
      location.reload();
    } else {
      this.router.navigateByUrl('/RefrshComponent', { skipLocationChange: true }).then(() =>
        this.router.navigate(["/course/" + courseId]));
    }
  }
}

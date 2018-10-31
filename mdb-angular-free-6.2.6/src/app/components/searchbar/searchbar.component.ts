import { Component, OnInit } from '@angular/core';
import {SearchbarService} from './searchbar.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.scss']
})
export class SearchbarComponent implements OnInit {
  COURSE_MATCHER = new RegExp("^[a-zA-Z]{3}[0-9]{1,3}$");
  course : string;
  
  // $(document).ready(function () {
  //     searchDropdown = new SearchDropdown();
  
  //     $('#courseSearch').on('input', function (e) {
  //         var input = this.value;
  //         if (input && input.length > 3 && COURSE_MATCHER.test(input)) {
  //             var URL = SEARCH_COURSE_API + input;
  //             $.get(URL, function (response) {
  //                 searchDropdown.initSearchDialog(response);
  //             });
  //             return true;
  //         }
  //         return false;
  //     });
  // });
  constructor(private searchbarService: SearchbarService) { }

  ngOnInit() {
  }

  checkValidInput(event: any) : boolean{
    if (this.course && this.course.length > 3  && this.COURSE_MATCHER.test(this.course)){
      console.log(this.course);
    }

    return true;
  }

}

import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// For MDB Angular Free
import { WavesModule, CardsFreeModule } from 'angular-bootstrap-md'

import { AppComponent } from './app.component';

import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DashboardComponent } from './views/dashboard/dashboard.component';
import { CourseCardComponent } from './components/course-card/course-card.component';
import { SearchbarComponent } from './components/searchbar/searchbar.component';
import { AppRoutingModule } from './app-routing.module';
import { CoursePageComponent } from './views/course-page/course-page.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { CommentComponent } from  './components/comment/comment.component';
import { ReadMoreComponent } from './components/read-more/read-more.component';
import { CommentDataService } from './components/comment/comment-data.service';
import { SearchbarService } from './components/searchbar/searchbar.service';
import { CourseCardDataService } from './components/course-card/course-card-data.service';
import { CoursePageDataService } from './views/course-page/course-page-data.service';


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    CourseCardComponent,
    SearchbarComponent,
    CoursePageComponent,
    SidebarComponent,
    CommentComponent,
    ReadMoreComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    WavesModule,
    CardsFreeModule,
    HttpClientModule,
    MDBBootstrapModule.forRoot(),
    FormsModule,
    AppRoutingModule,
  ],
  providers: [SearchbarService, CourseCardDataService, CoursePageDataService, CommentDataService],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }

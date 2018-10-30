import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// For MDB Angular Free
import { WavesModule, CardsFreeModule } from 'angular-bootstrap-md'

import { AppComponent } from './app.component';

import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CourseCardComponent } from './components/course-card/course-card.component';
import { CourseCardService } from './components/course-card/course-card.service';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    CourseCardComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    WavesModule,
    CardsFreeModule,
    HttpClientModule,
    MDBBootstrapModule.forRoot(),
    FormsModule,
  ],
  providers: [CourseCardService],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }

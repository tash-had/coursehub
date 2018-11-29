import { Component, AfterViewInit } from '@angular/core';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  title = 'app';
  loading: boolean;

  constructor(public auth: AuthService) {
    auth.handleAuthentication();
    this.loading = true;
  }

  /**
   * We are on Heroku's free tier, so the server sleeps
   * after 30 mins of inactivity. This code combined with the app module HTML
   * starts 
   */
  ngAfterViewInit() {
    this.auth.startAppServer()
      .subscribe((response) => {
        this.loading = false;
      });
  }
}

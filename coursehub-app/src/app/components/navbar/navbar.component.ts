import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  accountDropdownLabel: string = "My Account";

  constructor(public auth: AuthService, private _router: Router) { }

  ngOnInit() { 
    let username = localStorage.getItem("username");
    if (username != null && username != undefined && username != "undefined" && username.length > 0) {
      this.accountDropdownLabel = username;
    }  
  }

  navigateToDashboard(){
    if (this._router.url.toString().includes("search")) {
      location.reload();
    }
    else{
      this._router.navigate(['/search']);
    }
    
  }
  
}

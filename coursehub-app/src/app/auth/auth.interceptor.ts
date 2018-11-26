import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';

let AUTH_REQ_METHODS: string[] = ["GET", "POST", "PUT", "DELETE", "UPDATE"];

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept (req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    let idToken: string = localStorage.getItem("id_token");

    if (idToken == null || !AUTH_REQ_METHODS.includes(req.method) || !(req.url.includes("coursehub") && req.url.includes("api"))) {
        return next.handle(req);
    }
    const authReq = req.clone({
      headers: req.headers.set('Authorization', idToken)
    });
    return next.handle(authReq);
  }
}
import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

let AUTH_REQ_METHODS: string[] = ["POST", "PUT", "DELETE"];

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    let idToken: string = localStorage.getItem("id_token");

    if (idToken == null || !AUTH_REQ_METHODS.includes(req.method) || !(this.containsKeyword(req.url, environment.keywordsToIntercept))) {
      return next.handle(req);
    }
    const authReq = req.clone({
      headers: req.headers.set('Authorization', idToken)
    });
    return next.handle(authReq);
  }

  private containsKeyword(str: string, keywordArr: string[]): boolean {
    return keywordArr.some(substring => str.includes(substring));
  }
}
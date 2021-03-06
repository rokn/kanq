import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params, Router} from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import {Response} from '@angular/http';
import {FacebookService} from './facebook.service';
import {UserService} from '../../user/user.service';
import {Settings} from '../../settings';
import {isUndefined} from 'util';

@Component({
  template: 'Authenticating...'
})
export class FacebookTokenHandlerComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute,
              private router: Router,
              private facebookService: FacebookService,
              private userService: UserService) {}

  ngOnInit(): void {
    this.getFacebookToken();
  }

  private getFacebookToken() {
    this.activatedRoute.queryParams.subscribe((params: Params) => {
      this.facebookService.getToken(params['code'])
        .then(this.getAPIToken.bind(this));
    });
  }

  private getAPIToken(facebookToken: string) {
    this.userService.loginThroughToken(facebookToken, Settings.API_FACEBOOK_BACKEND)
      .then(this.saveAPIToken.bind(this));
  }

  private saveAPIToken(token: string) {
    if(token != undefined) {
      console.log('Facebook auth successful!', token);
      this.userService.handleLogin(token);
      this.router.navigate(['/']);
    }
    else {
      this.router.navigate(['/login']);
    }
  }
}

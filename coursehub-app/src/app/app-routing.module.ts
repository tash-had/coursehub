import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursePageComponent } from './course-page/course-page.component';
import { DashboardComponent } from './dashboard/dashboard.component';

const routes: Routes = [  {
  path: 'course-page',
  component: CoursePageComponent
},
{
  path: 'dashboard',
  component: DashboardComponent
},
{ path: '', redirectTo: '/dashboard', pathMatch: 'full' }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
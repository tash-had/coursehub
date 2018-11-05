import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursePageComponent } from './views/course-page/course-page.component';
import { DashboardComponent } from './views/dashboard/dashboard.component';

const routes: Routes = [  {
  path: 'course/:courseId',
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
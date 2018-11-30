import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursePageComponent } from './views/course-page/course-page.component';
import { DashboardComponent } from './views/dashboard/dashboard.component';
import { LoadingComponent } from './components/loading/loading.component';

const routes: Routes = [  {
  path: 'course/:courseId',
  component: CoursePageComponent
},
{
  path: 'search/:searchQuery',
  component: DashboardComponent
},
{ path: 'search', component: DashboardComponent},
{ path: '**', component: DashboardComponent},
{ path: '', redirectTo: '/search', pathMatch: 'full'},
{ path: 'callback', component: LoadingComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
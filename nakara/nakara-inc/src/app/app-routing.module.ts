import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PubComponent } from './view/pub/pub.component';
import { ObsComponent } from './view/obs/obs.component';

const routes: Routes = [
  { path: "publicador", component: PubComponent },
  { path: "observador", component: ObsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

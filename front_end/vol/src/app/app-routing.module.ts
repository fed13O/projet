import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { AjouterComponent } from './ajouter/ajouter.component';
import { ConsulterComponent } from './consulter/consulter.component';
import { HomeComponent } from './home/home.component';


const routes: Routes = [
  {path: 'home',component:HomeComponent},
  {path: 'About',component:AboutComponent},
  {path: 'Ajouter',component:AjouterComponent},
  {path: 'Consulter',component:ConsulterComponent},
  {path:'',component:HomeComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

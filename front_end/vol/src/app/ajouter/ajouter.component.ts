import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ajouter',
  templateUrl: './ajouter.component.html',
  styleUrls: ['./ajouter.component.css']
})
export class AjouterComponent implements OnInit {
  
  constructor() { }

  ngOnInit(): void {
  }
async add(){
  var id= (<HTMLInputElement> document.getElementById("id")).value;
  var date_dep= (<HTMLInputElement>document.getElementById("DateD")).value;
  var date_arr= (<HTMLInputElement>document.getElementById("DateA")).value;
  var heure_dep= (<HTMLInputElement>document.getElementById("heureD")).value;
  var heure_arr= (<HTMLInputElement>document.getElementById("heureA")).value;
  var ville_dep= (<HTMLInputElement>document.getElementById("villeD")).value;
  var ville_arr= (<HTMLInputElement>document.getElementById("villeA")).value;
  var prix= (<HTMLInputElement>document.getElementById("prix")).value;
  var nb= (<HTMLInputElement>document.getElementById("Nb")).value;
  var body = `{"id":"${id}" , "date_dep":"${date_dep}" , "date_arr":"${date_arr}" , "heure_dep":"${heure_dep}" ,"heure_arr":"${heure_arr}","ville_dep":"${ville_dep}","ville_arr":"${ville_arr}" , "prix":"${Number(prix)}","nb":"${nb}"}`
  const  rep = await fetch("http://127.0.0.1:8000/web/add",{
      method:"post",
      body:body
    })
    if (rep.ok){
    rep.json().then(data =>{
      console.log(data);
    })
  }


      //alert("succesful")
      window.location.reload()
    
    
   
  }
  

  

  

}
from typing import Optional
from fastapi import FastAPI , Request
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date
import mysql.connector
from fastapi.openapi.models import Response
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/web/add")
async def add(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "web")
    mycursor = mydb.cursor() 
    body = json.loads(await request.body())
    mycursor.execute(f"INSERT INTO vol (`id_vol`, `date_dep`, `date_arr`, `heure_dep`,`heure_arr`,`ville_dep`,`ville_arr`,`prix`,`nb_place`) VALUES ( '{body['id']}', '{body['date_dep']}', '{body['date_arr']}'  , '{body['heure_dep']}', '{body['heure_arr']}', '{body['ville_dep']}', '{body['ville_arr']}', '{body['prix']}', '{body['nb']}')")
    mydb.commit()
    return {"done"}
   
    
    
@app.get("/vol")
def get():#ken nheb naadi query param juste fi west el () nekteb b syntax hedha {esm_el_var}:{type} [EX : gets(id:int) ======> donc fel requete ki naamel get l http://127.0.0.1:8000/gets?id=4 el variable id mte3i fi west el code bech tkoun el valeur mte3ha 4]
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "web")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM vol")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data


@app.post("/web/supp")
async def supp(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "web")#Connectiw ala el BD mteena
    mycursor = mydb.cursor() 
    body = json.loads(await request.body())
    mycursor.execute(f"DELETE from vol where ( id_vol='{body['id']}')")
    mydb.commit()
    return {"done"}
   
@app.post("/web/modif")
async def add(request:Request):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "web")
    mycursor = mydb.cursor() 
    body = json.loads(await request.body())
    mycursor.execute(f"UPDATE `vol` SET `date_dep`='{body['date_dep']}',`date_arr`='{body['date_arr']}',`heure_dep`='{body['heure_dep']}',`heure_arr`='{body['heure_arr']}',`ville_dep`='{body['ville_dep']}',`ville_arr`='{body['ville_arr']}',`prix`={body['prix']},`nb_place`={body['nb_place']} where id_vol={body['id']}")
    mydb.commit()
    return {"done"}
      
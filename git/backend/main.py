from fastapi import security
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials #cuando nos conectemos a la api, va mostrar el usuario y el passwor es decir autentica 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from urllib.request import Request
from urllib import response
from lib2to3.pytree import Base
from typing import Union
from typing_extensions import Self
import hashlib
import sqlite3
import os
import pyrebase


app = FastAPI()

DATABASE_URL = os.path.join("sql/clientes.sqlite") #va formatear al texto al sistema operativo en donde lo corramos

firebaseConfig = {
    'apiKey': "AIzaSyC6UDpFIBmgveN0BQq1tK6WZH60hnOOn0E",
    'authDomain': "fir-api-70f5c.firebaseapp.com",
    'databaseURL': "https://fir-api-70f5c-default-rtdb.firebaseio.com",
    'projectId': "fir-api-70f5c",
    'storageBucket': "fir-api-70f5c.appspot.com",
    'messagingSenderId': "141856431030",
    'appId': "1:141856431030:web:2e796328394b9afd07bf17"
}
firebase = pyrebase.initialize_app(firebaseConfig)
securityBasic = HTTPBasic()
securityBearer = HTTPBearer()

class Usuarios(BaseModel):
    username: str
    level: int

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

class regcliente(BaseModel):
    nombre: str
    email : str

class ClienteIN(BaseModel):
    nombre: str
    email: str

origin =[
    "https://8000-nataly2102-aplicacionwe-kx8c8dnk4fb.ws-us60.gitpod.io/",
    "https://8080-nataly2102-aplicacionwe-kx8c8dnk4fb.ws-us60.gitpod.io/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=Respuesta)
async def index():
    return{"message":"Hello World"}
""" 
def get_current_level(credentials: HTTPBasicCredentials = Depends(security)): # va a recibir el password y nos va a regresar el 0 o un 1 si no lo encuentra nos dira usuario no encontrado
    password_b = hashlib.md5(credentials.password.encode())  #lo combierte MD5 y luego hace una consulta
    password = password_b.hexdigest() #lo combierte a hexadecimal
    with sqlite3.connect(DATABASE_URL) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT level FROM usuarios WHERE username = ? and password = ?",
            (credentials.username, password),
        )
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return user[0] """

@app.get("/clientes/", response_model=List[Cliente],status_code=status.HTTP_202_ACCEPTED,
summary="MUESTRA UNA LISTA DE USUARIO",description="MUESTRA UNA LISTA DE USUARIO")
async def clientes(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId'] 

        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM clientes')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)




@app.get("/clientes/{id_cliente}", response_model=List[Cliente],status_code=status.HTTP_202_ACCEPTED, summary="MUESTRA UNA LISTA DE CLIENTES SEGUN SU ID",description="MUESTRA UNA LISTA DE CLIENTES SEGUN SU ID")
async def clientes(credentials: HTTPAuthorizationCredentials = Depends(securityBearer),id_cliente: int=0):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId'] 

        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id_cliente={}".format(int(id_cliente)))
            response=cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="AGREGACION DE USUARIOS",description="AGREGACION DE USUARIOS")
async def post_cliente( cliente: ClienteIN, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId'] 

        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor=connection.cursor()
            cursor.execute("INSERT INTO clientes(nombre,email) VALUES(?,?)", (cliente.nombre,cliente.email))
            connection.commit()
            response = {"message":"Insertaste un cliente correctamente :)"}
            return response
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        


@app.put("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="ACTUALIZACION DE USUARIOS",description="ACTUALIZACION DE USUARIOS")
async def clientes_update(cliente: Cliente, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
     try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId'] 

        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("UPDATE clientes SET nombre =?, email= ? WHERE id_cliente =?;",(cliente.nombre, cliente.email, cliente.id_cliente))
            connection.commit()
            response = {"message":"Actualizaste un cliente correctamente :)"}
            return response
     except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)       


@app.delete("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="ELIMINACION DE USUARIOS",description="ELIMINACION DE USUARIOS")
async def clientes_delete(credentials: HTTPAuthorizationCredentials = Depends(securityBearer), id_cliente: int=0):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId'] 

        with sqlite3.connect('sql/clientes.sqlite') as connection:
            connection.row_factory = sqlite3.Row
            cursor=connection.cursor()
            cursor.execute("DELETE FROM clientes WHERE id_cliente = '{id_cliente}';".format(id_cliente=id_cliente))
            cursor.fetchall()
            response = {"message":"Eliminaste un cliente correctamente :("}
            return response
        
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)    

@app.get("/user/validate/",
         status_code=status.HTTP_202_ACCEPTED,
         summary="Mostrar tocken del usuario",
         description="Mosttrar tocken",
         tags=["auth"])
async def get_token(credentials: HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        response = {
            "token": user["idToken"],
        }
        return response
    except Exception as error:
        print(error)
@app.get("/users/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Get a  user",
    description ="Get a user",
    tags=["auth"])
async def get_user(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId']

        db = firebase.database()
        user_data = db.child("users").child(uid).get().val()

        response = {
            'user_data': user_data
        }
        return response
    except Exception as error:
        print(f"Error: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
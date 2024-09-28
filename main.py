from typing import Optional
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#http://127.0.0.1:8000
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message":"Hola, Pytonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data":id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message":f"libro {libro.titulo} insertado"}
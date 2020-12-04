from fastapi import FastAPI
from pydentic import BaseModel
from fastapi import HTTPException

appX = FastAPI()

class Animal(BaseModel):
    nombre: str
    tipo: str
    vuela: bool

bd ={
    "perro": Animal(nombre="perro", tipo="mamifero", vuela=false),
    "perro": Animal(nombre="pajaro", tipo="ave", vuela=true),
    "perro": Animal(nombre="vaca", tipo="mamifero", vuela=false)
}

@appX.get("/animales/{nombreAnimal}/")
async def consultar_animal(animal: str):
    if animal in bd:
        return[animal]
    else:
        raise HTTPException(staus_code=406, detail="Animal no existe")

    #pass
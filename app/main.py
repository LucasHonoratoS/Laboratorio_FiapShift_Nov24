from  typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/livro/livro_id")
def read_livro(livro_id: int, q:Union[str, None] = None):
    return {"item_id": item_id, "q": q}
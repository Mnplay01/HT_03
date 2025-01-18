import uvicorn
from typing import List
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

class GFILMS (BaseModel):
    id: int #id
    t1: str #title
    t2: str #synopsis
    p: bool = False #purchase info

films: List[GFILMS] = [
    GFILMS (id = 1, t1 = 'American Psycho', t2 = 'A wealthy New York City investment banking executive, Patrick Bateman, hides his alternate psychopathic ego from his co-workers and friends as he delves deeper into his violent, hedonistic fantasies.', p = False),
    GFILMS (id = 2, t1 = 'The Lighthouse', t2 = 'Two lighthouse keepers try to maintain their sanity while living on a remote and mysterious New England island in the 1890s.', p = False)   
]

@app.get("/")
async def welcum ():
    return Response (content='Welcome to the app ٩( ᐛ )و', media_type="text/plain")

@app.get("/all_films/", response_model = List[GFILMS])
async def all_films():
    return films

@app.get("/film_id/{ID}", response_model=GFILMS)
async def film_id(ID: int):
    for a in films:
        if a.id == ID : return a
    raise HTTPException(status_code=404, detail="Film with this ID can't be found!!!")

@app.get("/purchased_films", response_model=GFILMS)
async def purchased_films():
    A = []
    for a in films:
        if a.p == True : A += [a.t1]
    if len (A) != 0 : return A
    return Response (content="You haven't purchased any films yet!", media_type="text/plain")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_crudrouter import MemoryCRUDRouter


app = FastAPI()

class Emp(BaseModel):
    id: int
    name: str
    age: int
    salary: float

router = MemoryCRUDRouter(schema=Emp)
app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/emp/{id}")
def read_emp(id: int, q: str = None):
    return {"emp_id": id, "q": q}
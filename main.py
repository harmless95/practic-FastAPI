import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_hello():
    return {"message": "Hello world"}

@app.get("/name/")
def get_username(user: str = "User"):
    return {"message": f"Hello, {user}"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
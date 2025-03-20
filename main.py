from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb!"}

@app.get("/hola")
def read_root():
    return {"message": "Hello from Koyeb!"}

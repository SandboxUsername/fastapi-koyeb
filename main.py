from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# 1. Mount the 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. If you have an existing endpoint, e.g. /api/hello:
@app.get("/api/hello")
def hello_api():
    return {"message": "Hello from FastAPI!"}

# 3. Serve index.html at root path:
@app.get("/")
def root():
    # Return the index.html file in the static folder
    return FileResponse(os.path.join("static", "index.html"))

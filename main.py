from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import json

app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost",    # Allow requests from localhost (without port)
    "http://localhost:8000",    # Allow requests from localhost (without port)
    "http://localhost:1313"  # Allow requests from localhost with port 8000
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return [
        "2023-12-12",
        "2023-12-11"
    ]

class FormData(BaseModel):
    start: str
    end: str
    name: str
    mail: str
    title: str
    message: str

@app.post("/submit-form")
async def submit_form(request: Request):
    form_data = json.loads(await request.body())
    start = form_data["start"]
    end = form_data["end"]
    title = form_data["title"]
    mail = form_data["mail"]
    message = form_data["message"]

    print(start, message)
    # print(form_data)
    # Here, `blob_data` is the binary data received in the POST request.
    # You can process and manipulate the data as needed.
    # return JSONResponse(content={"message": "Blob received successfully"})
    pass

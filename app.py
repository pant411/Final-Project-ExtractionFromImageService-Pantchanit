# built in module
from typing import List, Union
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.middleware.cors import CORSMiddleware
# from werkzeug.utils import secure_filename
import cv2
import numpy as np
from pydantic import BaseModel, Field
from pydantic.schema import Optional
# my module
from mainModule import runMain # main application of project



app = FastAPI(title="My Final Project", debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return "Hello World!!!!"

@app.post("/receipts/uploadfile/submitreceipt", tags = ["Receipts"])
async def submitReceipt1(type_receipt: int = Form(...), 
                         file: UploadFile = File(...)):
    content_receipt = file.file.read()
    # print(content_receipt)
    image = cv2.imdecode(np.fromstring(content_receipt, np.uint8),\
            cv2.IMREAD_UNCHANGED)      
    data = runMain(image, type_receipt)
    return data

@app.post("/receipts/file/submitreceipt", tags = ["Receipts"])
async def submitReceipt2(type_receipt: int, 
                         file: bytes = File(...)): 
    image = cv2.imdecode(np.fromstring(file, np.uint8),\
            cv2.IMREAD_UNCHANGED)      
    data = runMain(image, type_receipt)
    return data

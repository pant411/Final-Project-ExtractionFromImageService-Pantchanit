# built in module
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
# from werkzeug.utils import secure_filename
import cv2
import numpy as np
# my module
from mainModule import runMain # main application of project

import pytesseract 

app = FastAPI(title="Extract text from receipt service!!!!!", debug=True)

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
    return "Extract text from receipt service!!!!!"

@app.get("/tesseractversion")
def tesseractVersion():
    return pytesseract.get_tesseract_version()

@app.post("/receipts/uploadfile/submitreceipt", tags = ["Receipts"])
async def submitReceipt1(file: UploadFile = File(...)):
    content_receipt = file.file.read()
    # print(content_receipt)
    image = cv2.imdecode(np.fromstring(content_receipt, np.uint8),\
            cv2.IMREAD_UNCHANGED)      
    data = runMain(image)
    return data

@app.post("/receipts/file/submitreceipt", tags = ["Receipts"])
async def submitReceipt2(file: bytes = File(...)): 
    image = cv2.imdecode(np.fromstring(file, np.uint8),\
            cv2.IMREAD_UNCHANGED)      
    data = runMain(image)
    return data



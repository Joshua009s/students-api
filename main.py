from fastapi import FastApi
from config import APPP_VERSION 

app=FastApi(title="stundets-api", version=APPP_VERSION)

@app.get("/healt")
def healt():
    return{"status":"ok"}
    
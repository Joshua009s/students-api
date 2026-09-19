from fastapi import FastApi
from config import APPP_VERSION 

app=FastApi(title="students-api", version=APPP_VERSION)

@app.get("/healt")
def healt():
    return {"status":"ok"}

@app.get("/students")
def list_students():
    return [{"id":1,"name":"John Doe"},{"id":2,"name":"Jane Smith"}]
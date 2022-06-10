from fastapi import FastAPI, Request
import json
app = FastAPI()

'''@app.post("/TestAPI")

async def root(info : Request):
    req_info = await info.json()
    return {"Response": "OK!"}'''

@app.get("/")
def root():
    return {"Message": "OK!"}

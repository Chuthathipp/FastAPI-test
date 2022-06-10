from fastapi import FastAPI, Request
import json
app = FastAPI()

@app.post("/TestAPI")

async def root(info : Request):
    req_info = await info.json()
    json_string = json.dumps(req_info)
    print(json_string)
    
    return {"Response": "OK!"}
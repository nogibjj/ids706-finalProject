from fastapi import FastAPI
import uvicorn
from dblib.dbquery import DB 
from urllib.parse import unquote

app = FastAPI()
db = DB() 

@app.get("/")
async def root():
    return "Welcome to the Educational Metrics Service!"

@app.get("/district_info/{district_name}")
async def get_district_info(district_name: str):
    decoded_district_name = unquote(district_name)
    return db.get_district_info(decoded_district_name)

@app.get("/all_districts_info")
async def get_all_districts_info():
    return db.get_all_districts_info()


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

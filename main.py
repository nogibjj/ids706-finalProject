from fastapi import FastAPI
import uvicorn
from dblib.dbquery import DB 
from urllib.parse import unquote

app = FastAPI()
db = DB() 

@app.get("/")
async def root():
    """Welcome message on homepage"""
    return "Welcome to the Educational Metrics Service!"

@app.get("/district_info/{district_name}")
async def get_district_info(district_name: str):
    """Return educational metrics for a specified school district"""
    decoded_district_name = unquote(district_name)  # Decodes URL-encoded strings
    return db.get_district_info(decoded_district_name)

@app.get("/all_districts_info")
async def get_all_districts_info():
    """Return summary info about all school districts"""
    return db.get_all_districts_info()

# Additional endpoints can be added here as needed

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

import logging
from fastapi import FastAPI
import uvicorn
from dblib.dbquery import DB 
from urllib.parse import unquote

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
db = DB() 

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return "Welcome to the Educational Metrics Service!"

@app.get("/district_info/{district_name}")
async def get_district_info(district_name: str):
    decoded_district_name = unquote(district_name)
    logger.info("Fetching district info for: %s", decoded_district_name)
    return db.get_district_info(decoded_district_name)

@app.get("/all_districts_info")
async def get_all_districts_info():
    logger.info("Fetching all districts info")
    return db.get_all_districts_info()

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

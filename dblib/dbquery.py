import json
import mysql.connector
import os
from decimal import Decimal
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(CustomJSONEncoder, self).default(obj)

class DB:
    """DB utility class to connect and query educational data"""
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),        
            user=os.getenv("DB_USER"),       
            passwd=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),         
            port=3306,   
        )
        self.cursor = self.connection.cursor()

    def get_district_info(self, district_name):
        try:
            """Return educational metrics for a specified school district"""
            query = f'SELECT * FROM school_districts WHERE School_District = "{district_name}"'
            self.cursor.execute(query)
            data = self.cursor.fetchall()

            columns = ['School_District', 'Average_Student_Teacher_Ratio', 'Percentage_of_High_School_Graduates', 
                    'Average_SAT_Score', 'Total_Number_of_Schools', 'Average_Technology_Integration_Score', 
                    'Total_Enrollment']
            result = [dict(zip(columns, row)) for row in data]
            logger.info("District info retrieved for %s", district_name)
            return json.dumps(result, cls=CustomJSONEncoder)
        except mysql.connector.Error as e:
            logger.error("Database error: %s", e)        

        except Exception as e:
            logger.error("Error retrieving district info for %s: %s", district_name, e)
            raise


    def get_all_districts_info(self):
        try:
            """Return summary info about all school districts"""
            query = 'SELECT * FROM school_districts'
            self.cursor.execute(query)
            data = self.cursor.fetchall()

            columns = ['School_District', 'Average_Student_Teacher_Ratio', 'Percentage_of_High_School_Graduates', 
                    'Average_SAT_Score', 'Total_Number_of_Schools', 'Average_Technology_Integration_Score', 
                    'Total_Enrollment']
            result = [dict(zip(columns, row)) for row in data]
            logger.info("All districts info retrieved")
            return json.dumps(result, cls=CustomJSONEncoder)

        except mysql.connector.Error as e:
            logger.error("Database error: %s", e)

        except Exception as e:
            logger.error("Error retrieving all districts info: %s", e)
            raise

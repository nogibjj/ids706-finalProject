"""Database query lib"""
import json
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
        """Return educational metrics for a specified school district"""
        query = f'SELECT * FROM school_districts WHERE School_District = "{district_name}"'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        columns = ['School_District', 'Average_Student_Teacher_Ratio', 'Percentage_of_High_School_Graduates', 
                   'Average_SAT_Score', 'Total_Number_of_Schools', 'Average_Technology_Integration_Score', 
                   'Total_Enrollment']
        result = [dict(zip(columns, row)) for row in data]
        return json.dumps(result)

    def get_all_districts_info(self):
        """Return summary info about all school districts"""
        query = 'SELECT * FROM school_districts'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        columns = ['School_District', 'Average_Student_Teacher_Ratio', 'Percentage_of_High_School_Graduates', 
                   'Average_SAT_Score', 'Total_Number_of_Schools', 'Average_Technology_Integration_Score', 
                   'Total_Enrollment']
        result = [dict(zip(columns, row)) for row in data]
        return json.dumps(result)

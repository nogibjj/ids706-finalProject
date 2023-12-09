import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306,
    )

def save_data(connection, row):
    cursor = connection.cursor()
    district, student_teacher_ratio, graduation_percent, sat_score, total_schools, tech_score, total_enrollment = row

    # Process percentage and NA values
    # If the value is already a float, we won't perform string operations on it
    student_teacher_ratio = float(student_teacher_ratio) if student_teacher_ratio != 'NA' else None
    
    # Check if graduation_percent is a string and contains '%', then process
    if isinstance(graduation_percent, str) and '%' in graduation_percent:
        graduation_percent = float(graduation_percent.strip('%')) / 100
    else:
        graduation_percent = None if graduation_percent == 'NA' else float(graduation_percent)

    sat_score = int(sat_score) if sat_score != 'NA' else None
    total_schools = int(total_schools) if total_schools != 'NA' else None
    tech_score = float(tech_score) if tech_score != 'NA' else None
    total_enrollment = int(total_enrollment) if total_enrollment != 'NA' else None

    values = (district, student_teacher_ratio, graduation_percent, sat_score, total_schools, tech_score, total_enrollment)
    query = "INSERT INTO school_districts (School_District, Average_Student_Teacher_Ratio, Percentage_of_High_School_Graduates, Average_SAT_Score, Total_Number_of_Schools, Average_Technology_Integration_Score, Total_Enrollment) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, values)
    connection.commit()

def save_all_data():
    df = pd.read_csv("./school_districts.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        try:
            save_data(connection, row)
        except Exception as e:
            print(f"Error in row {index}: {e}")
            continue
    connection.close()

if __name__ == "__main__":
    save_all_data()

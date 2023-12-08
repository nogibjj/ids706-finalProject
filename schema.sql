CREATE TABLE school_districts (
    School_District VARCHAR(255) NOT NULL,
    Average_Student_Teacher_Ratio DECIMAL(5, 2), 
    Percentage_of_High_School_Graduates DECIMAL(5, 2), 
    Average_SAT_Score INT,  
    Total_Number_of_Schools INT,
    Average_Technology_Integration_Score DECIMAL(3, 2),  
    Total_Enrollment INT,  
    PRIMARY KEY (School_District)
);

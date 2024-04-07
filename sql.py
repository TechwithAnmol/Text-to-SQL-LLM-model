from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()

table_info = """
Create table EMPLOYEE(NAME VARCHAR(25), DEPARTMENT VARCHAR(25), LOCATION VARCHAR(30), RATING INT);
"""
# cursor.execute(table_info)

cursor.execute('''Insert Into EMPLOYEE values('Anmol','Data Science','New York',90)''')
cursor.execute('''Insert Into EMPLOYEE values('Angad','Web Development','Chicago',100)''')
cursor.execute('''Insert Into EMPLOYEE values('Siddhaant','Data Science','Boston',86)''')
cursor.execute('''Insert Into EMPLOYEE values('Arjun','Web Development','Tampa',80)''')
cursor.execute('''Insert Into EMPLOYEE values('Abhijeet','Gamer','Orlando',85)''')
cursor.execute('''Insert Into EMPLOYEE values('Shivam','Gamer','Ohio',97)''')

print("Inserted records are")

data = cursor.execute("SELECT * FROM EMPLOYEE")
for i in data:
    print(i)

connection.commit()
connection.close()
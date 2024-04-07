from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import sqlite3
load_dotenv() 

genai.configure(api_key = os.getenv("API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for i in rows:
        print(i)
    return rows

# prompt = [
#     """
#     you are an expert in converting English to SQL query!The SQL database has the name EMPLOYEE and has the following columns - NAME, DEPARTMENT, LOCATION, RATING \n\n 
#     For Example, \n
#     Example 1 - How many entries of records are present?,
#     the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE;\n
#     Example 2 -  What are the names of all employees?,
#     the SQL command will be something like this SELECT Name FROM EMPLOYEE; \n
#     Example 3 - Which city does each employee work in?,
#     the SQL command will be something like this SELECT Name, City FROM EMPLOYEE; \n
#     Example 4 - List the employees working in 'Web Development' with a score above 85
#     the SQL command will be something like this SELECT Name FROM EMPLOYEE WHERE JobRole = 'Web Development' AND Score > 85; \n
#     also the sql code should not have ``` in beginning or end and sql word should not be in the output either  
#     """
# ]
prompt = [
    """
    you are an expert in converting English to SQL query!The SQL database has the name DATA and has the following columns - UserID, Age, Gender, VRHeadset, Duration, MotionSickness, ImmersionLevel \n\n 
    There are three types of headsets, HTC Vive, Oculus Rift and PlayStation VR. The genders are Male, Female and others. Duration is a decimal number in seconds. Motion sickness and immersion levels are numerical rating out of 10.
    For Example, \n
    Example 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM DATA;\n
    Example 2 - Retrieve interaction details for HTC Vive,
    the SQL command will be something like this SELECT * FROM DATA WHERE VRHeadset = 'HTC Vive';; \n
    Example 3 - Retrieve all distinct genders from the database,
    the SQL command will be something like this SELECT DISTINCT Gender FROM DATA; \n
    Example 4 - Calculate the average duration of interactions
    the SQL command will be something like this SELECT AVG(Duration) FROM DATA; \n
    Example 5 - Find users experiencing motion sickness 
    the SQL command will be something like this SELECT UserID, MotionSickness FROM DATA WHERE MotionSickness; \n
    Example 6 - what are the average duration of interactions for each VR headset type
    the SQL command will be something like this SELECT VRHeadset, AVG(Duration) AS AverageDuration FROM DATA GROUP BY VRHeadset; \n
    also the sql code should not have ``` in beginning or end and sql word should not be in the output either  
    """
]

st.set_page_config(page_title="Finally making text to sql work")
st.header("Retrieve Data of the study done on users for VR headsets")
st.header("The data we have today is Age, Gender, Type of Headsets, Immersion Levels, Motion Sickness levels and the time each user used it for")
question = st.text_input("Ask anything about the database: ", key = "Ask anything about the database: ")
submit = st.button("ask the question")
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "Data.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)

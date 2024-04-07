# Text-to-SQL-LLM-model

Text-to-SQL-LLM-model is a personal project aimed at allowing users to input natural language text instead of SQL queries to retrieve data. The project utilizes Google Gemini Pro models for text-to-SQL conversion.

## Installation

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
Functions
sql.py: This module enables users to create their own SQL database.

csvToSql.py: Use this script to convert CSV data into SQL format and create a corresponding database.

app.py: This is the main application file where users can interact with the text-to-SQL functionality.

Usage
Start by installing the dependencies with pip install -r requirements.txt.
Use sql.py to create your desired SQL database schema.
Convert CSV data into SQL format and create a database using csvToSql.py.
Run app.py to interact with the text-to-SQL model by inputting natural language queries.

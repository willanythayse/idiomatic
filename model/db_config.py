#############################################
#   Autho   Thayse Jordao 
#   Date    05/31/2024
#############################################
import cx_Oracle
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection parameters from environment variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
dsn = os.getenv('DB_DSN')
encoding = os.getenv('DB_ENCODING')

# Check the environment variables
if not all([username,password,dsn]):
    raise ValueError("One or more required environment variables are missing")

# Config the database connection
def config_connection():

    """Create and return a new database connection."""
    connection = cx_Oracle.connect(
        user=username,
        password=password,
        dsn=dsn,
        encoding=encoding
    )
    
    return connection

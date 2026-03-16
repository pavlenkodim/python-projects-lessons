import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_USER_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"))
        return connection
    except (Exception, Error) as error:
        print("Error create DB", error)


# Create DB
def create_database():
    try:
        connection = create_connection()

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()

        sql_create_database = 'create database postgres'

        cursor.execute(sql_create_database)

    except (Exception, Error) as error:
        print("Error create DB", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# get parametrs from DB
def get_parameters_from_database():
    try:
        connection = create_connection()

        cursor = connection.cursor()
        print('information from database',
              connection.get_dsn_parameters(),
              '\n',
              cursor.execute("SELECT version();"))

        record = cursor.fetchone()

        print('You connected to - ', record, "\n")

    except (Exception, Error) as error:
        print("Error create DB", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

get_parameters_from_database()
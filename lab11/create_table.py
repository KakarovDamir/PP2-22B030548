import psycopg2
from config import config

try:
    params = config()
    connection = psycopg2.connect(**params)

    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE TSIS11(
            Name varchar(20) NOT NULL,
            Number varchar(20) NOT NULL)"""
        )
        print("[INFO]: Table created successfully")  


except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if connection:
        connection.close()
        print("[INFO]:PostgreSQL connection closed")
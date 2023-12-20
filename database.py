import mysql.connector as mysql_connector
import os
env = os.environ

def create_database_connection():
    try:
        return mysql_connector.connect(user=env.get("DbUser"),
                                       password=env.get("DbPass"),
                                       host=env.get("DbHost"),
                                       database=env.get("DbDatabase"))
    except Exception as e:
        print(e)
        return None

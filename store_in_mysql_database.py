import json
from database import create_database_connection
from constants import IS_ON_WINDOWS
# MySQL Connection
# CREATE TABLE TestData (
#     recordId INT AUTO_INCREMENT PRIMARY KEY,
#     topic VARCHAR(120),
#     payload VARCHAR(1000),
#     createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
def store_in_my_sql_database(topic, payload, timestamp):
    try:
        if not IS_ON_WINDOWS:
            query = "INSERT INTO TestData (topic, payload, createdAt) VALUES (%s, %s)"
            values = (topic, payload, timestamp)

            mysql_conn = create_database_connection()
            mysql_cursor = mysql_conn.cursor()
            mysql_cursor.execute(query, values)
            mysql_conn.commit()
            mysql_conn.close()
            mysql_cursor.close()
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

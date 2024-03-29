#!/usr/bin/python3
"""
    module for state model filteration
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # connection parameters
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    host = 'localhost'
    port = 3306

    # database connection
    conn = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        db=database
        )
    # grab the cursor to access the database
    cursor = conn.cursor()
    query = f'SELECT * FROM `states` ORDER BY states.id'

    # query executation
    cursor.execute(query)

    # access the fetched data
    rows = cursor.fetchall()

    # DISPLAY RESULT
    for key, value in rows:
        if value[0] == 'N':
            print((key, value))

    cursor.close()
    conn.close()

#!/usr/bin/python3
"""
    module for state filter given name
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # connection parameters
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    search = args[4]
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
    query = "SELECT cities.name FROM cities INNER JOIN states \
    ON cities.state_id = states.id WHERE BINARY states.name = '{}' \
    ORDER BY states.id".format(search)

    # query executation
    cursor.execute(query)

    # access the fetched data
    rows = cursor.fetchall()

    # DISPLAY RESULT
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

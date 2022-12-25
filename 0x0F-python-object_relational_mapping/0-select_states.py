#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = args[1], args[2], args[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    t = r.fetch_row(maxrows=0)
    for i in t:
        print(i)
 

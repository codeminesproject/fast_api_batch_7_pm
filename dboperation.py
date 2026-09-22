
from dbconnection import connection

def insert(query):
    dbconnect = connection()
    if type(dbconnect).__name__=="Connection":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return dbconnect

def update(query):
    dbconnect = connection()
    if type(dbconnect).__name__=="Connection":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return dbconnect

def delete(query):
    dbconnect = connection()
    if type(dbconnect).__name__=="Connection":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return dbconnect

def getSingleData(query):
    dbconnect = connection()
    if type(dbconnect).__name__=="Connection":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        return data
    else:
        return dbconnect

def getAllData(query):
    dbconnect = connection()
    if type(dbconnect).__name__=="Connection":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    else:
        return dbconnect
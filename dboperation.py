
from dbconnection import connection

def insert(query):
    dbconnect = connection()
    if dbconnect is not None:
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return None

def update(query):
    dbconnect = connection()
    if dbconnect is not None:
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return None

def delete(query):
    dbconnect = connection()
    if dbconnect is not None:
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return None

def getSingleData(query):
    dbconnect = connection()
    if dbconnect is not None:
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        return data
    else:
        return None

def getAllData(query):
    dbconnect = connection()
    if dbconnect is not None:
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    else:
        return None
import pymysql
import config

def connection():
    try:
        dbconnect = pymysql.connect(host=config.hostname,port=config.port,user=config.username,password=config.password,database=config.dbname)
        if dbconnect.open:
            return dbconnect
        else:
            return None
    except Exception as e:
        return None

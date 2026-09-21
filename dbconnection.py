import pymysql
import config
import CommonModule

def connection():
    try:
        dbconnect = pymysql.connect(host=config.hostname,port=config.port,user=config.username,password=config.password,database=config.dbname)
        if dbconnect.open:
            return dbconnect
        else:
            return None
    except Exception as e:
        CommonModule.Error.type = type(e).__name__
        CommonModule.Error.message = str(e)
        CommonModule.Error.file_name = "dbconnection"
        CommonModule.Error.function_name = "connection"
        return CommonModule.Error

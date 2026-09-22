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
        error_obj = CommonModule.Error()
        error_obj.type = type(e).__name__
        error_obj.message = str(e)
        error_obj.file_name = "dbconnection"
        error_obj.function_name = "connection"
        return error_obj

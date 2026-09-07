from fastapi import FastAPI

# create object of FastApi
obj = FastAPI()

@obj.get("/display-message")
def displayMessage():
    return {"message":"Welcome to CodeMines Computer"}

@obj.get("/display-all-students")
def displayAllStudents():
    student_list = [
        {"id":1,"name":"Ishika","address":"Mumbai"},
        {"id":2,"name":"Veena","address":"Mumbai"},
        {"id":3,"name":"Komal","address":"Bhayander"},
        {"id":4,"name":"Rekha","address":"Borivali"},
        {"id":5,"name":"Apeksha","address":"Vasai"},
        {"id":6,"name":"Ankita","address":"Dahisar"}
    ]
    return {"data":student_list}

@obj.get("/get-student-by-id")
def displayStudentById(id:int):
    student_list = [
        {"id":1,"name":"Ishika","address":"Mumbai"},
        {"id":2,"name":"Veena","address":"Mumbai"},
        {"id":3,"name":"Komal","address":"Bhayander"},
        {"id":4,"name":"Rekha","address":"Borivali"},
        {"id":5,"name":"Apeksha","address":"Vasai"},
        {"id":6,"name":"Ankita","address":"Dahisar"}
    ]

    for student in student_list:
        if student["id"]==id:
            return {"data":student}

    return {"message":"No record found"}

@obj.get("/display-student-details")
def getStudentDetails(id:int,name:str,address:str):
    student_data = {"id":id,"student_name":name,"student_address":address}
    return {"data":student_data}

@obj.get("/get-student-by-id-path/{id}")
def displayStudentByIdPath(id:int):
    student_list = [
        {"id":1,"name":"Ishika","address":"Mumbai"},
        {"id":2,"name":"Veena","address":"Mumbai"},
        {"id":3,"name":"Komal","address":"Bhayander"},
        {"id":4,"name":"Rekha","address":"Borivali"},
        {"id":5,"name":"Apeksha","address":"Vasai"},
        {"id":6,"name":"Ankita","address":"Dahisar"}
    ]

    for student in student_list:
        if student["id"]==id:
            return {"data":student}

    return {"message":"No record found"}

@obj.get("/display-student-details-path/{id}/{name}/{address}")
def getStudentDetailsPath(id:int,name:str,address:str):
    student_data = {"id":id,"student_name":name,"student_address":address}
    return {"data":student_data}

@obj.get("/display-student-details-path-optional/{id}/{name}/{address}")
def getStudentDetailsPathOptional(id:int,name:str="",address:str=""):
    student_data = {"id":id,"student_name":name,"student_address":address}
    return {"data":student_data}




from fastapi import FastAPI,Body
from dboperation import getAllData,insert,getSingleData,delete,update
from pydantic import BaseModel

# create object of FastApi
obj = FastAPI()

class RegisterRequest(BaseModel):
    name:str
    email:str
    mobile:str
    password:str
    role:str

class UpdatePasswordRequest(BaseModel):
    username:str
    password:str

class AuthRequest(BaseModel):
    id:int
    password:str

@obj.get("/get-all-users")
def getAllUsers():
    query = "select * from user_login"
    db_response = getAllData(query)
    if db_response is not None:
        if len(db_response)>0:
            user_list = []
            for data in db_response:
                response = {
                    "id":data[0],
                    "name":data[1],
                    "email":data[2],
                    "mobile":data[3],
                    "password":data[4],
                    "role":data[5]
                }
                user_list.append(response)
            return {"data":user_list}
        else:
            return {"data":"no record found"}
    else:
        return {"data":"something went wrong"}

@obj.post("/register")
def registerNewUser(request:RegisterRequest):
    print("name:",request.name)
    query = f"INSERT INTO user_login (name, email, mobile, password, role) VALUES('{request.name}', '{request.email}', '{request.mobile}', '{request.password}', '{request.role}')"
    db_response = insert(query)
    if db_response is not None:
        return {"data":"record inserted succesfully"}
    else:
        return {"data":"something went wrong"}

@obj.get("/get-user-by-email")
def getUserByEmail(email):
    query = f"select * from user_login where email='{email}'"
    db_response = getSingleData(query)
    if db_response is not None:
        response = {
                    "id":db_response[0],
                    "name":db_response[1],
                    "email":db_response[2],
                    "mobile":db_response[3],
                    "password":db_response[4],
                    "role":db_response[5]
                    }
        return {"data":response}
    else:
        return {"data":"something went wrong"}

@obj.delete("/delete-user")
def deleteUser(id):
    query = f"delete from user_login where id = {id}"
    db_response = delete(query)
    if db_response is not None:
        return {"data":"record deleted succesfully"}
    else:
        return {"data":"something went wrong"}

@obj.put("/update-user")
def updatePassword(request:UpdatePasswordRequest):
    query = f"update user_login set password='{request.password}' where id = {request.id}"
    db_response = update(query)
    if db_response is not None:
        return {"data":"record updated succesfully"}
    else:
        return {"data":"something went wrong"}

@obj.post("/auth")
def userLogin(request:UpdatePasswordRequest):
    query = f"select * from user_login where email='{request.username}' and password='{request.password}'"
    db_response = getSingleData(query)
    if db_response is not None:
        return {"data":"Login Successfull"}
    else:
        return {"data":"invalid username or password"}
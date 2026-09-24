from fastapi import FastAPI,Body,Request
from dboperation import getAllData,insert,getSingleData,delete,update
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from jose import jwt
from datetime import datetime,timedelta,timezone

# create object of FastApi
obj = FastAPI(title="Student Management System API",
              description="prepared by CodeMines Brilliant Minds",
              version="1.0.0")

CLIENT_SECRET_CODE = "codeminescomputerinstitute"
ALGORITHM = "HS256"

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

@obj.get("/get-all-users",summary="Used to fetch all users data",tags=["User"])
def getAllUsers(request:Request):
    try:
        auth_token = request.headers.get("Authorization")
        
        auth_token = auth_token.replace("Bearer ","")
        
        response_data = jwt.decode(auth_token,CLIENT_SECRET_CODE,algorithms=[ALGORITHM])
        print(response_data)

        query = "select * from user_login"
        db_response = getAllData(query)
        if type(db_response).__name__ != "Error":
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
                return JSONResponse(status_code=200,content={"data":user_list}) 
            else:
                return JSONResponse(status_code=404,content={"data":"no record found"})
        else:
            return JSONResponse(
                status_code=500,
                content={"message":"something went wrong",
                        "error_type":db_response.type,
                        "error_message":db_response.message,
                        "error_file_name":db_response.file_name,
                        "error_function_name":db_response.function_name,}
                ) 
    except:
        return JSONResponse(
                        status_code=500,
                        content={"message":"Invalid Token"}
                        ) 

@obj.post("/register",summary="Register New User",tags=["User"])
def registerNewUser(request:RegisterRequest):

    isEmailExist = checkEmailExist(request.email)
    if isEmailExist==True:
        return JSONResponse(status_code=400,content={"message":"email already exist"})

    isMobileExist = checkMobileNumberExist(request.mobile)
    if isMobileExist==True:
        return JSONResponse(status_code=400,content={"message":"mobile number already exist"})
    

    query = f"INSERT INTO user_login (name, email, mobile, password, role) VALUES('{request.name}', '{request.email}', '{request.mobile}', '{request.password}', '{request.role}')"
    db_response = insert(query)
    if type(db_response).__name__ != "Error":
        return JSONResponse(status_code=201,content={"data":"record inserted succesfully"})
    else:
        return JSONResponse(
                    status_code=500,
                    content={"message":"something went wrong",
                             "error_type":db_response.type,
                             "error_message":db_response.message,
                             "error_file_name":db_response.file_name,
                             "error_function_name":db_response.function_name,}
                    ) 

def checkEmailExist(email):
    query = f"select * from user_login where email='{email}'"
    db_response = getSingleData(query)
    if db_response is not None:
        return True
    else:
        return False

def checkMobileNumberExist(mobile):
    query = f"select * from user_login where mobile='{mobile}'"
    db_response = getSingleData(query)
    if db_response is not None:
        return True
    else:
        return False
        

@obj.get("/get-user-by-email",summary="Fetch user details using email id",tags=["User"])
def getUserByEmail(email):
    query = f"select * from user_login where email='{email}'"
    db_response = getSingleData(query)
    if type(db_response).__name__ != "Error":
        if db_response is not None:
            response = {
                        "id":db_response[0],
                        "name":db_response[1],
                        "email":db_response[2],
                        "mobile":db_response[3],
                        "password":db_response[4],
                        "role":db_response[5]
                        }
            return JSONResponse(status_code=200,content={"data":response})
        else:
            return JSONResponse(status_code=404,content={"data":"no record found"})
    else:
        return JSONResponse(
                            status_code=500,
                            content={"message":"something went wrong",
                                     "error_type":db_response.type,
                                     "error_message":db_response.message,
                                     "error_file_name":db_response.file_name,
                                     "error_function_name":db_response.function_name,}
                            ) 

@obj.delete("/delete-user",tags=["User"])
def deleteUser(id):
    query = f"delete from user_login where id = {id}"
    db_response = delete(query)
    if db_response is not None:
        return {"data":"record deleted succesfully"}
    else:
        return {"data":"something went wrong"}

@obj.put("/update-user",tags=["User"])
def updatePassword(request:UpdatePasswordRequest):
    query = f"update user_login set password='{request.password}' where id = {request.id}"
    db_response = update(query)
    if db_response is not None:
        return {"data":"record updated succesfully"}
    else:
        return {"data":"something went wrong"}

@obj.post("/auth",tags=["User"])
def userLogin(request:UpdatePasswordRequest):
    isEmailExist = checkEmailExist(request.username)
    if isEmailExist==False:
        return JSONResponse(status_code=400,content={"message":"email not registered"})
    
    query = f"select * from user_login where email='{request.username}' and password='{request.password}'"
    db_response = getSingleData(query)
    if type(db_response).__name__ != "Error":
        if db_response is not None:
            response = {
                                    "id":db_response[0],
                                    "name":db_response[1],
                                    "email":db_response[2],
                                    "mobile":db_response[3],
                                    "password":db_response[4],
                                    "role":db_response[5]
                                    }
            expiry_date = datetime.now(timezone.utc)+ timedelta(minutes=2)

            data_response = {"data":response,"exp":expiry_date}

            jwt_token = jwt.encode(data_response,CLIENT_SECRET_CODE,ALGORITHM)
            
            return JSONResponse(status_code=200,content={"data":jwt_token})
        else:
            return JSONResponse(status_code=401,content={"data":"invalid username or password"})
    else:
            return JSONResponse(
                                status_code=500,
                                content={"message":"something went wrong",
                                         "error_type":db_response.type,
                                         "error_message":db_response.message,
                                         "error_file_name":db_response.file_name,
                                         "error_function_name":db_response.function_name,}
                                )

@obj.get("/get-account-details",tags=["Account"])
def accountDetails(email):
    query = f"select * from user_login where email='{email}'"
    db_response = getSingleData(query)
    if type(db_response).__name__ != "Error":
        if db_response is not None:
            print(db_response[5])
            if db_response[5]=="admin":
                return JSONResponse(status_code=200,content={"data":"account report fetched successfully"})
            else:
                return JSONResponse(status_code=403,content={"data":"you are not authorised to fetch account details"})
        else:
                return JSONResponse(status_code=404,content={"data":"no record found"})
    else:
        return JSONResponse(
                                status_code=500,
                                content={"message":"something went wrong",
                                         "error_type":db_response.type,
                                         "error_message":db_response.message,
                                         "error_file_name":db_response.file_name,
                                         "error_function_name":db_response.function_name,}
                                ) 
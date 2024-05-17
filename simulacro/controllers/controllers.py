from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
#from db.db import SessionLocal
from auth.role import RoleChecker
from pydantic import BaseModel
from simulacro.services.services import Simulacros
from config.db import SessionLocal
from sqlalchemy.orm import Session
from auth.jwt_bearer import JwtBearer
import base64
import os
# import pyodbc  
# print(pyodbc.drivers())

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/average/area", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],)
async def average_by_area(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)):
    answer = Simulacros().average_by_area(code, year, test, grade, classroom, db)
    return answer

@router.get("/average/subject/classroom", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],) 
async def average_by_subject_classroom(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().average_by_subject_classroom(code, year, test, grade, classroom, db)
        return _answer
    except Exception as e:
        return []

@router.get("/area/performance", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],) 
async def area_performance(code: int, year: int, test: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().area_performance(code, year, test, grade)
        return _answer
    except Exception as e:
        return []
    

@router.get("/performance-level/students", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],) 
async def performance_level_by_students(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().performance_level_by_students(code, year, test, grade, classroom, db)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/subject", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],)
async def desviation_by_subject(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_subject(code, year, test, grade, classroom, db)
        return _answer
    except Exception as e:
        return []
    
@router.get("/notes/competencies", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],)
async def notes_by_competencies(code: int, year: int, test: int, grade: int, classroom: int, subject: int, ID_student: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_competencies(code, year, test, grade, classroom, subject, ID_student, db)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/competencies", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],) 
async def desviation_by_competencies(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_competencies(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/notes/components", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],)
async def notes_by_components(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_components(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/components", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],) 
async def desviation_by_components(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_components(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
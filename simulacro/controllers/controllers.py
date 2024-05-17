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

@router.get("/global/params", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) #dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))],
async def global_params(code: int, year: int, db: Session = Depends(get_db)):
    global_params = Simulacros().get_global_params(code, year, db)
    
    if not global_params:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    return global_params

@router.get("/board/average/area", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) 
async def board_averagebyArea(code: int, year: int, simulacrum: int, grade: int, classroom: int, db: Session = Depends(get_db)):
    
    try:
        _answer = Simulacros().get_board_averagebyArea(code, year, simulacrum, grade, classroom, db)
        return _answer
    except Exception as e:
        return []

@router.get("/board/subject/classroom", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def board_subject_classroom(code: int, year: int, simulacrum: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_board_subject_classroom(code, year, simulacrum, grade, classroom, db)
        return _answer
    except Exception as e:
        return []

@router.get("/board/area/performance", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def board_area_performance(code: int, year: int, simulacrum: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_board_area_performance(code, year, simulacrum, grade)
        return _answer
    except Exception as e:
        return []
    

@router.get("/analysisSubject/percentage/students" , status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
}) 
async def percentage_students_performanceLvel(code: int, simulacrum: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_percentage_students_performanceLvel(code, simulacrum, grade, classroom, db)
        return _answer
    except Exception as e:
        return []

    
@router.get("/analysisSubject/deviation/subject", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def desviation_subject(code: int, year: int, simulacrum: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_desviation_subject(code, year, simulacrum, grade, classroom)
        return _answer
    except Exception as e:
        return []

@router.get("/competencies/students/notes", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def competencies_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_competencies_students_notes(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
        
@router.get("/competencies/deviation/competencies", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def competencies_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_competencies_deviation(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    

@router.get("/components/students/notes", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def components_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
        
    try:
        _answer = Simulacros().get_components_students_notes(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    

@router.get("/components/deviation/competencies", status_code=status.HTTP_200_OK, responses={
    200: {"description": "Successful Response"},
    404: {"description": "Resource not found"},
    500: {"description": "Internal Server Error"}
})
async def components_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_components_deviation(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
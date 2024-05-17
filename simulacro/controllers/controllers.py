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

@router.get("/board/average/area")
async def board_averagebyArea(code: int, year: int, simulacrum: int, grade: int, classroom: int, db: Session = Depends(get_db)):
    
    try:
        _answer = Simulacros().get_board_averagebyArea(code, year, simulacrum, grade, classroom, db)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}

@router.get("/board/subject/classroom") 
async def board_subject_classroom(code: int, year: int, simulacrum: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().average_by_subject_classroom(code, year, test, grade, classroom, db)
        return _answer
    except Exception as e:
        return []

@router.get("/board/area/performance") 
async def board_area_performance(code: int, year: int, simulacrum: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().area_performance(code, year, test, grade)
        return _answer
    except Exception as e:
        return []
    

@router.get("/analysisSubject/percentage/students") 
async def percentage_students_performanceLvel(code: int, year: int, simulacrum: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().get_percentage_students_performanceLvel(code, year, simulacrum, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.get("/analysisSubject/deviation/subject")
async def desviation_subject(code: int, year: int, simulacrum: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_subject(code, year, test, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.get("/competencies/students/notes")
async def competencies_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_competencies(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/competencies/deviation/competencies") 
async def competencies_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_competencies(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    

@router.get("/components/students/notes")
async def components_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_components(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/components/deviation/competencies") 
async def components_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_components(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
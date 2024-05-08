from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
#from db.db import SessionLocal
from pydantic import BaseModel
from simulacro.services.services import example
from sqlalchemy.orm import Session
import base64
import os

router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.post("/board/average/area")
async def board_averagebyArea(code: int, year: int, simulacrum: int, grade: int):
    
    try:
        _answer = example().get_board_averagebyArea(code, year, simulacrum, grade)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}

@router.post("/board/subject/classroom") 
async def board_subject_classroom(code: int, year: int, simulacrum: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_board_subject_classroom(code, year, simulacrum, grade)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}


@router.post("/board/area/performance") 
async def board_area_performance(code: int, year: int, simulacrum: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_board_area_performance(code, year, simulacrum, grade)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}

@router.post("/analysisSubject/percentage/students") 
async def percentage_students_performanceLvel(code: int, year: int, simulacrum: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_percentage_students_performanceLvel(code, year, simulacrum, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.post("/analysisSubject/deviation/subject")
async def desviation_subject(code: int, year: int, simulacrum: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_desviation_subject(code, year, simulacrum, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.post("/competencies/students/notes")
async def competencies_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_competencies_students_notes(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.post("/competencies/deviation/competencies") 
async def competencies_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_competencies_deviation(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    

@router.post("/components/students/notes")
async def components_students_notes(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_components_students_notes(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.post("/components/deviation/competencies") 
async def components_deviation(code: int, year: int, simulacrum: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = example().get_components_deviation(code, year, simulacrum, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []    
    

# @router_pensar.get("/competencies", dependencies=[Depends(JwtBearer()), Depends(RoleChecker(allowed_roles=["DIR_INS"]))], status_code=status.HTTP_200_OK, responses={   
#                     200: {"description": "Successful Response"},
#                     404: {"description": "Resource not found"},
#                     500: {"description": "Internal Server Error"}
#                 })
# async def competences(code: int, year: int, 
#                     grade: Union[int, None] = None, 
#                     classroom: Union[str, None] = None, 
#                     idCompetence: Union[int, None] = None, 
#                     idArea: Union[int, None] = None, 
#                     db: Session = Depends(get_db)):
    
#     _competencia = Ppensar().competences_calculate(code, year, grade, classroom, idCompetence, idArea, db)
#     # if not _competencia:
#     #     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Competencie not found")
#     return _competencia
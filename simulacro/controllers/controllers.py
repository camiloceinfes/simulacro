from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
#from db.db import SessionLocal
from pydantic import BaseModel
from simulacro.services.services import Simulacros
from config.db import SessionLocal
from sqlalchemy.orm import Session
import base64
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/average/area")
async def average_by_area(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)):
    answer = Simulacros().average_by_area(code, year, test, grade, classroom, db)
    return answer

@router.get("/average/subject/classroom") 
async def average_by_subject_classroom(code: int, year: int, test: int, grade: int, classroom: int, db: Session = Depends(get_db)): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().average_by_subject_classroom(code, year, test, grade, classroom, db)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}


@router.get("/area/performance") 
async def area_performance(code: int, year: int, test: int, grade: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().area_performance(code, year, test, grade)
        return _answer
    except Exception as e:
        return []
        #return {"error": str(e)}

@router.get("/performance-level/students") 
async def performance_level_by_students(code: int, year: int, test: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().performance_level_by_students(code, year, test, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/subject")
async def desviation_by_subject(code: int, year: int, test: int, grade: int, classroom: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_subject(code, year, test, grade, classroom)
        return _answer
    except Exception as e:
        return []
    
@router.get("/notes/competencies")
async def notes_by_competencies(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_competencies(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/competencies") 
async def desviation_by_competencies(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_competencies(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    

@router.get("/notes/components")
async def notes_by_components(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().notes_by_components(code, year, test, grade, classroom, subject)
        return _answer
    except Exception as e:
        return []
    
@router.get("/desviation/components") 
async def desviation_by_components(code: int, year: int, test: int, grade: int, classroom: int, subject: int): #, db: Session = Depends(get_db)
    
    try:
        _answer = Simulacros().desviation_by_components(code, year, test, grade, classroom, subject)
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
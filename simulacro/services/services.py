from sqlalchemy.orm import sessionmaker
#from models.models import purchases
from dotenv import load_dotenv
from datetime import datetime
#from db.db import engine
# import uuid
# import json
# import os

class example():
  def get_board_averagebyArea(self, code, year, simulacrum, grade):

    columns = [
        { 'headerName': 'Promedio', 'field': 'promedio', 
        },
        { 'headerName': 'Matemáticas', 'field': 'matematicas', 
        },
        { 'headerName': 'Sociales Y Ciudadanas', 'field': 'socialesCiudadanas', 
        },
        { 'headerName': 'Ciencias Naturales', 'field': 'cienciasNaturales', 
        },
        { 'headerName': 'Lectura Crítica', 'field': 'lecturaCritica', 
        },
        { 'headerName': 'Inglés', 'field': 'ingles', 
        },
        { 'headerName': 'Definitiva', 'field': 'definitiva', 
        },
        { 'headerName': 'Global', 'field': 'global', 
        },
    ]
    
    #lista = []
    
    lista = [{
            "id": 1,
            "promedio": 'Mejores promedios',
            "matematicas": 90,
            "socialesCiudadanas": 80,
            "cienciasNaturales": 70,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40
        },
        {
            "id": 2,
            "promedio": 'Nacional',
            "matematicas": 90,
            "socialesCiudadanas": 80,
            "cienciasNaturales": 70,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40
        },
        {
            "id": 3,
            "promedio": 'Ciudad',
            "matematicas": 90,
            "socialesCiudadanas": 80,
            "cienciasNaturales": 70,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40
        },
        {
            "id": 4,
            "promedio": 'Plantel',
            "matematicas": 90,
            "socialesCiudadanas": 80,
            "cienciasNaturales": 70,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40
        }
      ]
    
    return {'columns': columns, 'rows': lista}
  
  def get_board_subject_classroom(self, code, year, simulacrum, grade ):

    columns = [
        { 'headerName': 'Grado', 'field': 'grado', 
        },
        { 'headerName': 'Salón', 'field': 'salon', 
        },
        { 'headerName': 'Prueba', 'field': 'prueba', 
        },
        { 'headerName': 'Genéricos', 'field': 'genericos', 
        },
        { 'headerName': 'No Genéricos', 'field': 'noGenericos', 
        },
        { 'headerName': 'Química', 'field': 'quimica', 
        },
        { 'headerName': 'Física', 'field': 'fisica', 
        },
        { 'headerName': 'Biología', 'field': 'biologia', 
        },
        { 'headerName': 'Ciencia, tecn y soc', 'field': 'cts', 
        },
        { 'headerName': 'Lectura Crítica', 'field': 'lecturaCritica', 
        },
        { 'headerName': 'Inglés', 'field': 'ingles', 
        },
        { 'headerName': 'Definitiva', 'field': 'definitiva', 
        },
        { 'headerName': 'Global', 'field': 'global', 
        },
      ]
    
    #lista = []
    
    lista = [{
            "id": 1,
            "grado": 9,
            "salon": 2,
            "Prueba": 'Prueba Pensar',
            "genericos": 90,
            "noGenericos": 90,
            "quimica": 90,
            "fisica": 90,
            "biologia": 90,
            "cts": 90,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40,
            "global": 90,
        },
        {
            "id": 2,
            "grado": 8,
            "salon": 2,
            "Prueba": 'Prueba Pensar',
            "genericos": 90,
            "noGenericos": 90,
            "quimica": 90,
            "fisica": 90,
            "biologia": 90,
            "cts": 90,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40,
            "global": 90,
        },
        {
            "id": 3,
            "grado": 7,
            "salon": 2,
            "Prueba": 'Prueba Pensar',
            "genericos": 90,
            "noGenericos": 90,
            "quimica": 90,
            "fisica": 90,
            "biologia": 90,
            "cts": 90,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40,
            "global": 90,
        },
        {
            "id": 4,
            "grado": 6,
            "salon": 2,
            "Prueba": 'Prueba Pensar',
            "genericos": 90,
            "noGenericos": 90,
            "quimica": 90,
            "fisica": 90,
            "biologia": 90,
            "cts": 90,
            "lecturaCritica": 60,
            "ingles": 50,
            "definitiva": 40,
            "global": 90,
          }
        ]
    
    return {'columns': columns, 'rows': lista}
  
  def get_board_area_performance(self, code, year, simulacrum, grade):

    #labels = []; datasets = []; label = []; data = []
    
    data = {
            "labels":[
                "Ciencias naturales",
                "Inglés",
                "Sociales y Ciudadanas",
                "Lectura Critica",
                "Matemáticas"
            ],
            "datasets":[
                {
                  "label":"nombreSimulacro | Grado: 10 | Salón 34",
                  "data":[65, 59, 90, 81, 56, 55, 40]
                }
            ]
          }
    return data

  def get_percentage_students_performanceLvel(self, code, year, simulacrum, grade, classroom):

    data = {
      'totalStudents': 'number',
      'data': {
      'title': 'string',
      'labels': [ 'Razonamiento', 'Conocimientos', 'Quimica', 'Fisica'],
      'datasets': [
          {
            'label': 'Bajo',
            'data': [0, 20, 30, 40],
            'backgroundColor': '#DC3D3D',
          },
          {
            'label': 'Básico',
            'data': [0, 20, 30, 40],
            'backgroundColor': '#E27E1E',
          },
          {
            'label': 'Alto',
            'data': [0, 20, 30, 40],
            'backgroundColor': 'rgba(241, 204, 48, 1)',
          },
              {
            'label': 'Superior',
            'data': [0, 20, 30, 40],
            'backgroundColor': 'rgba(146, 185, 59, 0.7)',
          },
        ]
      }
    }
  
    return data
  
  def get_desviation_subject(self, code, year, simulacrum, grade, classroom):

    columns = [
        { 'headerName': 'Materia', 'field': 'materia', 
        },
        { 'headerName': 'Promedio', 'field': 'promedio', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacion', 
        },
        { 'headerName': 'Min. Valor', 'field': 'valorMinimo', 
        },
        { 'headerName': 'Max. Valor', 'field': 'valorMaximo', 
        },
      ]
    
    #lista = []
    
    lista = [{
            "id": 1,
            "materia": 'Inglés',
            "promedio": 90,
            "desviacion": 80,
            "valorMinimo": 70,
            "valorMaximo": 60,
        },
        {
            "id": 2,
            "materia": 'Sociales',
            "promedio": 90,
            "desviacion": 80,
            "valorMinimo": 70,
            "valorMaximo": 60,
        },
        {
            "id": 3,
            "materia": 'Matematicas',
            "promedio": 90,
            "desviacion": 80,
            "valorMinimo": 70,
            "valorMaximo": 60,
        },
        {
            "id": 4,
            "materia": 'Lectura critica',
            "promedio": 90,
            "desviacion": 80,
            "valorMinimo": 70,
            "valorMaximo": 60,
          }
        ]
    
    return {'columns': columns, 'rows': lista}
  
  def get_competencies_students_notes(self, code, year, simulacrum, grade, classroom, subject):

    columns = [
        { 'headerName': 'Estudiante', 'field': 'estudiante', 
        },
        { 'headerName': 'Grado', 'field': 'grado', 
        },
        { 'headerName': 'Salón', 'field': 'salon', 
        },
        { 'headerName': 'Prueba', 'field': 'prueba', 
        },
        { 'headerName': 'Materia', 'field': 'materia', 
        },
        { 'headerName': 'Competencia', 'field': 'competencia', 
        },
        { 'headerName': 'Nota', 'field': 'nota', 
        },
        { 'headerName': 'Preguntas', 'field': 'preguntas', 
        },
      ]

    lista = [{
            "id": 1,
            "estudiante": 'Pedro Pérez',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 2,
            "estudiante": 'Pedro Martinez',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 3,
            "estudiante": 'Pedro Infante',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 4,
            "estudiante": 'Pedro Solano',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },  
      ]

    return {'columns': columns, 'rows': lista}
  
  def get_competencies_deviation(self, code, year, simulacrum, grade, classroom, subject):

    columns = [
        { 'headerName': 'Materia', 'field': 'materia', 
        },
        { 'headerName': 'Competencia', 'field': 'competencia', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioNacional', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionNacional', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioDpto', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionDpto', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioCiudad', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionCiudad', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioPlantel', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionPlantel', 
        }
      ]

    lista = [{
            "id": 1,
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 2,
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 3,
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 4,
            "materia": 'Inglés',
            "competencia": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        }
      ]

    return {'columns': columns, 'rows': lista}
  
  def get_components_students_notes(self, code, year, simulacrum, grade, classroom, subject):

    columns = [
        { 'headerName': 'Estudiante', 'field': 'estudiante', 
        },
        { 'headerName': 'Grado', 'field': 'grado', 
        },
        { 'headerName': 'Salón', 'field': 'salon', 
        },
        { 'headerName': 'Prueba', 'field': 'prueba', 
        },
        { 'headerName': 'Materia', 'field': 'materia', 
        },
        { 'headerName': 'Componente', 'field': 'componente', 
        },
        { 'headerName': 'Nota', 'field': 'nota', 
        },
        { 'headerName': 'Preguntas', 'field': 'preguntas', 
        },
      ]

    lista = [{
            "id": 1,
            "estudiante": 'Pedro Pérez',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 2,
            "estudiante": 'Pedro Martinez',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 3,
            "estudiante": 'Pedro Infante',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },
        {
            "id": 4,
            "estudiante": 'Pedro Solano',
            "grado": 9,
            "salon": 2,
            "prueba": 'Prueba pensar',
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "nota": 4,
            "preguntas": 20
        },  
      ]

    return {'columns': columns, 'rows': lista}
  
  def get_components_deviation(self, code, year, simulacrum, grade, classroom, subject):

    columns = [
        { 'headerName': 'Materia', 'field': 'materia', 
        },
        { 'headerName': 'Componente', 'field': 'componente', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioNacional', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionNacional', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioDpto', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionDpto', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioCiudad', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionCiudad', 
        },
        { 'headerName': 'Promedio', 'field': 'promedioPlantel', 
        },
        { 'headerName': 'Desviación', 'field': 'desviacionPlantel', 
        }
      ]

    lista = [{
            "id": 1,
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 2,
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 3,
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        },
        {
            "id": 4,
            "materia": 'Inglés',
            "componente": 'Comunicativa',
            "promedioNacional": 60,
            "desviacionNacional": 20,
            "promedioDpto": 60,
            "desviacionDpto": 20,
            "promedioCiudad": 60,
            "desviacionCiudad": 20,
            "promedioPlantel": 60,
            "desviacionPlantel": 20,            
        }
      ]

    return {'columns': columns, 'rows': lista}
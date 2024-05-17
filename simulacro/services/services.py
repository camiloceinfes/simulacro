from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
import polars as pl
import pandas as pd
import json

class Simulacros():

  def get_global_params(self, code, year, db):
      procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Pensar_EnlazaaParametrosGenerales"
      
      try:
          query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno")
          result = db.execute(query, {"Codigo": code, "Anno": year }).fetchall()

          #print(json.loads(result[0][0]))
          #result = json.loads(result[0][0])
          result_iterable = json.loads(result[0][0])['grades']

          lista = []
          list_cycles = []
          unique_list = []
          for i in result_iterable:
              lista.append(i['scholarcycle']['name'])

          for j in lista:
              if j not in unique_list:
                  unique_list.append(j)
          for i in unique_list: 
              cycles = {'id': unique_list.index(i)+1, "name": i, "alias": i}
              list_cycles.append(cycles)
          
          cycles = {'cycles': list_cycles}

          result_dict = json.loads(result[0][0])
          result_dict.update(cycles)

          return result_dict
      
      except Exception as e:
          print(f'error {e}')
          raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
      
  def get_board_averagebyArea(self, code, year, simulacrum, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PromedioColegioArea"
  
    try:
      query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Grado=:Grado, @Salon=:Salon, @Prueba=:Prueba")
      result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": simulacrum}).fetchall()
      
      #print(result)
      if len(result) != 0:

        df = pl.DataFrame(result)

        columns = [
            { 'headerName': 'Promedio', 'field': 'promedio', 
            },
            { 'headerName': 'Matemáticas', 'field': 'matematicas',
            },
            { 'headerName': 'Ciencias Naturales', 'field': 'cienciasNaturales',  
            },
            { 'headerName': 'Sociales Y Ciudadanas', 'field': 'socialesCiudadanas', 
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
                  
        data = {
                'Promedio': df['column_0'].apply(lambda x: x[0]),
                'Matemáticas': df['column_0'].apply(lambda x: x[1]),
                'Ciencias Naturales': df['column_0'].apply(lambda x: x[2]),
                'Sociales Y Ciudadanas': df['column_0'].apply(lambda x: x[3]),
                'Lectura Crítica': df['column_0'].apply(lambda x: x[4]),
                'Inglés': df['column_0'].apply(lambda x: x[5]),
                'Definitiva': df['column_0'].apply(lambda x: x[6]),
                'Global': df['column_0'].apply(lambda x: x[7]),
                'ID': df['column_0'].apply(lambda x: x[8])
              }
        new_df = pd.DataFrame(data)
        new_df = new_df.fillna(0)
        new_df = new_df.to_dict(orient='records')

        lista = []

        for elemento in new_df:
        
            dicc = {
                    "id": elemento['ID'],
                    "promedio": elemento['Promedio'],
                    "matematicas": elemento['Matemáticas'],
                    "cienciasNaturales": elemento['Ciencias Naturales'],
                    "socialesCiudadanas": elemento['Sociales Y Ciudadanas'],
                    "lecturaCritica": elemento['Lectura Crítica'],
                    "ingles": elemento['Inglés'],
                    "definitiva": elemento['Definitiva'],
                    "global": elemento['Global']
                }
        
            lista.append(dicc)

        return {'columns': columns, 'rows': lista}
    except Exception as e:
        print(f'error {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

  def get_board_subject_classroom(self, code, year, simulacrum, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PromedioColegioSalon"
  
    try:
        query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Grado=:Grado, @Salon=:Salon, @Prueba=:Prueba")
        result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": simulacrum}).fetchall()
        
        if len(result) != 0:

          df = pl.DataFrame(result)

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
            { 'headerName': 'Sociales', 'field': 'sociales', 
            },
            { 'headerName': 'Ciudadanas', 'field': 'ciudadanas', 
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
          #print(result)

          data = {
                  'Grado': df['column_0'].apply(lambda x: x[0]),
                  'Salón': df['column_0'].apply(lambda x: x[1]),
                  'Prueba': df['column_0'].apply(lambda x: x[2]),
                  'Genéricos': df['column_0'].apply(lambda x: x[3]),
                  'No Genéricos': df['column_0'].apply(lambda x: x[4]),
                  'Química': df['column_0'].apply(lambda x: x[5]),
                  'Física': df['column_0'].apply(lambda x: x[6]),
                  'Biología': df['column_0'].apply(lambda x: x[7]),
                  'Ciencia, tecn y soc': df['column_0'].apply(lambda x: x[8]),
                  'Sociales': df['column_0'].apply(lambda x: x[9]),
                  'Ciudadanas': df['column_0'].apply(lambda x: x[10]),
                  'Lectura Crítica': df['column_0'].apply(lambda x: x[11]),
                  'Inglés': df['column_0'].apply(lambda x: x[12]),
                  'Definitiva': df['column_0'].apply(lambda x: x[13]),
                  'Global': df['column_0'].apply(lambda x: x[14]),
                  'ID': df['column_0'].apply(lambda x: x[15])
                }
          
          new_df = pd.DataFrame(data)
          new_df = new_df.fillna(0)
          new_df = new_df.to_dict(orient='records')

          lista = []

          for elemento in new_df:
          
              dicc = {
                      "id": elemento['ID'],
                      "grado": elemento['Grado'],
                      "salon": elemento['Salón'],
                      "prueba": elemento['Prueba'],
                      "genericos": elemento['Genéricos'],
                      "noGenericos": elemento['No Genéricos'],
                      "quimica": elemento['Química'],
                      "fisica": elemento['Física'],
                      "biologia": elemento['Biología'],
                      "cts": elemento['Ciencia, tecn y soc'],
                      "ciudadanas": elemento['Ciudadanas'],
                      "lecturaCritica": elemento['Lectura Crítica'],
                      "ingles": elemento['Inglés'],
                      "definitiva": elemento['Definitiva'],
                      "global": elemento['Global'],
                  }
          
              lista.append(dicc)

          #print(lista)
          return {'columns': columns, 'rows': lista}

          #return 'prueba'
    
    except Exception as e:
        print(f'error {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
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

  def get_percentage_students_performanceLvel(self, code, simulacrum, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PorcentajeEstudiantePorNivelDesempeno"
  
    try:
        query = text(f"EXEC {procedure_name} @Codigo=:Codigo,  @Prueba=:Prueba, @Grado=:Grado, @Salon=:Salon")
        result = db.execute(query, {"Codigo": code, "Grado": grade, "Salon": classroom, "Prueba": simulacrum}).fetchall()

        print(result)

        if len(result) != 0:

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
        
    except Exception as e:
        print(f'error {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
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
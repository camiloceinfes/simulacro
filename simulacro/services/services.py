from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
import polars as pl
import pandas as pd
import json

class Simulacros():
  def average_by_area(self, code, year, test, grade, classroom, db):
    #print('entro aqui');
    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PromedioColegioArea"
  
    try:
      query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Grado=:Grado, @Salon=:Salon, @Prueba=:Prueba")
      result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": test}).fetchall()
      
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

  def average_by_subject_classroom(self, code, year, test, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PromedioColegioSalon"
  
    try:
        query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Grado=:Grado, @Salon=:Salon, @Prueba=:Prueba")
        result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": test}).fetchall()
        
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


          return {'columns': columns, 'rows': lista}
    except Exception as e:
        print(f'error {e}')
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
  def area_performance(self, code, year, test, grade):
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

  def performance_level_by_students(self, code, year, test, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_PorcentajeEstudiantePorNivelDesempeno"
  
    try:

      query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Prueba=:Prueba, @Grado=:Grado, @Salon=:Salon")
      result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": test}).fetchall()

      if len(result) != 0:
        #print(result)

        labels_list = []; Low_performance = []; basic_performance = []
        high_performance = []; superior_performance = []
        

        for iterator in result:
          labels_list.append(iterator[0])
          Low_performance.append(iterator[2])
          basic_performance.append(iterator[4])
          high_performance.append(iterator[6])
          superior_performance.append(iterator[8])

        data = {
          'totalStudents': 'number',
          'data': {
          'title': 'string',
          'labels': labels_list,
          'datasets': [
              {
                'label': 'Bajo',
                'data': Low_performance,
                'backgroundColor': '#DC3D3D',
              },
              {
                'label': 'Básico',
                'data': basic_performance,
                'backgroundColor': '#E27E1E',
              },
              {
                'label': 'Alto',
                'data': high_performance,
                'backgroundColor': 'rgba(241, 204, 48, 1)',
              },
                  {
                'label': 'Superior',
                'data': superior_performance,
                'backgroundColor': 'rgba(146, 185, 59, 0.7)',
              },
            ]
          }
        }
      
        #return {'columns': columns, 'rows': lista}
      return data  
    except Exception as e:
      print(f'error {e}')
      return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
  
  def desviation_by_subject(self, code, year, test, grade, classroom, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_DesviacionPorMaterias"
  
    try:

      query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Prueba=:Prueba, @Grado=:Grado, @Salon=:Salon")
      result = db.execute(query, {"Codigo": code, "Anno": year, "Grado": grade, "Salon": classroom, "Prueba": test}).fetchall()
      #print(result)
      df = pl.DataFrame(result)

      if len(result) != 0:

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
        
        data = {
                'Materia': df['column_0'].apply(lambda x: x[0]),
                'Promedio': df['column_0'].apply(lambda x: x[1]),
                'Desviación': df['column_0'].apply(lambda x: x[2]),
                'Min. Valor': df['column_0'].apply(lambda x: x[3]),
                'Max. Valor': df['column_0'].apply(lambda x: x[4]),
                'ID': df['column_0'].apply(lambda x: x[5]),
              }
        
        new_df = pd.DataFrame(data)
        new_df = new_df.fillna(0)
        new_df = new_df.to_dict(orient='records')

        lista = []

        for elemento in new_df:
        
            dicc = {
                    "id": elemento['ID'],
                    "materia": elemento['Materia'],
                    "promedio": elemento['Promedio'],
                    "desviacion": elemento['Desviación'],
                    "valorMinimo": elemento['Min. Valor'],
                    "valorMaximo": elemento['Max. Valor'],
                  }
        
            lista.append(dicc)

        return {'columns': columns, 'rows': lista}
    except Exception as e:
      print(f'error {e}')
      return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
  def notes_by_competencies(self, code, year, test, grade, classroom, subject, ID_student, db):

    procedure_name = "BD_MARTESDEPRUEBA.dbo.SPR_Simulacros_NotasEstudiantesPorCompetencias"
    # FALTA ID
    try:

      query = text(f"EXEC {procedure_name} @Codigo=:Codigo, @Anno=:Anno, @Prueba=:Prueba, @Grado=:Grado, @Salon=:Salon, @CodigoMateria=:CodigoMateria, @IDestudiante=:IDestudiante")
      result = db.execute(query, {"Codigo": code, "Anno": year, "Prueba": test, "Grado": grade, "Salon": classroom, "CodigoMateria": subject, "IDestudiante": ID_student}).fetchall()
      #print(result)
      df = pl.DataFrame(result)

      if len(result) != 0:

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
        
        data = {
                'Estudiante': df['column_0'].apply(lambda x: x[0]),
                'Grado': df['column_0'].apply(lambda x: x[1]),
                'Salón': df['column_0'].apply(lambda x: x[2]),
                'Prueba': df['column_0'].apply(lambda x: x[3]),
                'Materia': df['column_0'].apply(lambda x: x[4]),
                'Competencia': df['column_0'].apply(lambda x: x[5]),
                'Nota': df['column_0'].apply(lambda x: x[6]),
                'Preguntas': df['column_0'].apply(lambda x: x[7]),
              }
        
        new_df = pd.DataFrame(data)
        new_df = new_df.fillna(0)
        new_df = new_df.to_dict(orient='records')

        lista = []

        for elemento in new_df:
        
            dicc = {
                    "estudiante": elemento['Estudiante'],
                    "grado": elemento['Grado'],
                    "promedio": elemento['Salón'],
                    "prueba": elemento['Prueba'],
                    "materia": elemento['Materia'],
                    "competencia": elemento['Competencia'],
                    "nota": elemento['Nota'],
                    "preguntas": elemento['Preguntas'],
                  }
        
            lista.append(dicc)

        return {'columns': columns, 'rows': lista}
        #return {'columns': columns, 'rows': lista}
    except Exception as e:
      print(f'error {e}')
      return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="Internal Server Error")
  
  def desviation_by_competencies(self, code, year, test, grade, classroom, subject):

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
  
  def notes_by_components(self, code, year, test, grade, classroom, subject):

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
  
  def desviation_by_components(self, code, year, test, grade, classroom, subject):

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
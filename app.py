from fastapi import FastAPI
#from db.db import Base, engine
from simulacro.controllers.controllers import router
import simulacro.models.models as pen

app = FastAPI()

#pen.Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api", tags=["Simulacro"])
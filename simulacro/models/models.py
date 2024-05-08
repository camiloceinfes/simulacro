from sqlalchemy import  Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
#from db.db import Base

Base = declarative_base()
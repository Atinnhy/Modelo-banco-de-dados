import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src import Base, relationship


class GenderEnum(enum.Enum):
    MALE = "Homem"
    FEMALE = "Mulher"
    OTHER = "Outro"

class Employee(Base):
    __tablename__ = "TbEmployee"

    id = Column (Integer, primary_key=True)
    first_name = Column (String(50), nullable=False)
    last_name = Column (String(50), nullable=False)
    age = Column (Integer, nullable=False)
    gender = Column (Enum(GenderEnum), nullable=False)
    salary = Column (Integer, nullable=False)
    
    position_id = Column(Integer, ForeignKey("TbPosition.position_id"))
    position = relationship("Position", back_populates="employees")

class Position(Base):
    __tablename__ = "TbPosition"

    position_id = Column (Integer, primary_key=True)
    position_name = Column (String(50), nullable=False)
    position_description = Column (String(50), nullable=False)
    position_workload = Column (Integer, nullable=False)

    employees = relationship("Employee", back_populates="position")

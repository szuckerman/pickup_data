from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pickup_data.config import engine

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    family_id = Column(Integer, ForeignKey('family.id'))

    purchases = relationship("Purchase", back_populates="student")
    teacher = relationship("Teacher", back_populates="student")
    family = relationship("Family", back_populates="student")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    grade = Column(String)
    gender = Column(String)

    student = relationship("Student", back_populates="teacher")


class Family(Base):
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    phone_number = Column(String)
    email_address = Column(String)

    student = relationship("Student", back_populates="family")


class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    order_id = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))
    purchase_timestamp = Column(DateTime)
    quantity = Column(Integer)
    total_cost = Column(Float)

    student = relationship("Student", back_populates="purchases")
    item = relationship("Item", back_populates="purchases")


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    item_type = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="item")


Base.metadata.create_all(engine)
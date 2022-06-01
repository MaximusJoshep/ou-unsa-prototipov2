from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/prototipo'
db=SQLAlchemy(app)

class Persona(db.Model):
    __tablename__= 'persona'
    id_persona=db.Column(db.Integer, primary_key=True)
    comun_profesion=db.Column(db.Text, nullable=False)
    departamento=db.Column(db.Text, nullable=False)
    direccion=db.Column(db.Text, nullable=False)
    distrito=db.Column(db.Text, nullable=False)
    edad=db.Column(db.Integer, nullable=False)
    etnia=db.Column(db.Text, nullable=False)
    latitud=db.Column(db.Float, nullable=False)
    longitud=db.Column(db.Float, nullable=False)
    provincia=db.Column(db.Text, nullable=False)
    tiene_sintomas =db.Column(db.Text, nullable=False)
    tipo_documento=db.Column(db.Text, nullable=False)
    comun_sexo_paciente=db.Column(db.Text, nullable=False)
    domicilio_residencia=db.Column(db.Text, nullable=False)
    fecha_registro=db.Column(db.DateTime, nullable=False)

def format_persona(persona):
    return {
        "id": persona.id_persona,
        "profesion": persona.comun_profesion,
        "departemento": persona.departamento,
        "direccion": persona.direccion,
        "distrito": persona.distrito,
        "edad": persona.edad,
        "etnia": persona.etnia,
        "latitud": persona.latitud,
        "longitud": persona.longitud,
        "provincia": persona.provincia,
        "Tiene sintomas": persona.tiene_sintomas,
        "Tipo de documento": persona.tipo_documento,
        "sexo": persona.comun_sexo_paciente,
        "domicilio": persona.domicilio_residencia,
        "fecha de registro": persona.fecha_registro 
    }
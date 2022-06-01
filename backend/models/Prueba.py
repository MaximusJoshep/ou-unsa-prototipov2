from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/prototipo'
db=SQLAlchemy(app)

class Prueba(db.Model):
    __tablename__= "prueba"
    id_prueba=db.Column(db.Integer, primary_key=True)
    tipo_prueba=db.Column(db.Text, nullable=False)
    tipo_muestra=db.Column(db.Text, nullable=False)
    tipo_lectura=db.Column(db.Text, nullable=False)
    estado_de_la_prueba=db.Column(db.Text, nullable=False)
    fecha_ejecucion=db.Column(db.DateTime, nullable=False)
    fecha_registro=db.Column(db.DateTime, nullable=False)
    lugar_registra=db.Column(db.Text, nullable=False)
    resultado=db.Column(db.Text, nullable=False)
    cod_establecimiento_ejecuta=db.Column(db.Text, nullable=False)
    cod_establecimiento_registra=db.Column(db.Text, nullable=False)
    establecimiento_ejecuta=db.Column(db.Text, nullable=False)
    clasificacion_clinica=db.Column(db.Text, nullable=False)
    lugar_salud=db.Column(db.Text, nullable=False)

def format_prueba(prueba):
    return {
        "id": prueba.id_prueba,
        "tipo de prueba": prueba.tipo_prueba,
        "tipo de muestra": prueba.tipo_muestra,
        "tipo de lectura": prueba.tipo_lectura,
        "estado": prueba.estado_de_la_prueba,
        "fecha de ejecucion": prueba.fecha_ejecucion,
        "fecha de registro": prueba.fecha_registro,
        "clasificacion clinica": prueba.clasificacion_clinica,
        "lugar_salud": prueba.lugar_salud,
        "registra": prueba.lugar_registra,
        "resultado": prueba.resultado,
        "codigo del establecimiento que ejecuta": prueba.cod_establecimiento_ejecuta,
        "codigo del establecimiento que registra": prueba.cod_establecimiento_registra,
        "establecimiento que ejecuta": prueba.establecimiento_ejecuta       
    }
    

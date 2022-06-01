from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/prototipo'
db=SQLAlchemy(app)

class Tiempo(db.Model):
    __tablename__ = 'tiempo'
    id_tiempo=db.Column(db.Integer, primary_key=True)
    anio_ejecucion=db.Column(db.Integer,nullable=False)
    mes_ejecucion=db.Column(db.Integer,nullable=False)
    dia_ejecucion=db.Column(db.Integer,nullable=False)
    anio_registro=db.Column(db.Integer,nullable=False)
    mes_registro=db.Column(db.Integer,nullable=False)
    dia_registro=db.Column(db.Integer,nullable=False)


def format_tiempo(tiempo):
     return{
         "id": tiempo.id_tiempo,
         "anio ejecucion": tiempo.anio_ejecucion,
         "mes ejecucion": tiempo.mes_ejecucion,
         "dia ejecucion": tiempo.dia_ejecucion,
         "anio registro": tiempo.anio_registro,
         "mes registro": tiempo.mes_registro,
         "dia registro": tiempo.dia_registro
     }
if __name__=='__main__':
    app.run()
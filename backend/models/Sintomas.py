from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:pacris23@localhost/prototipo'
db=SQLAlchemy(app)

class Sintomas(db.Model):
    __tablename__="sintomas"
    id_sintomas=db.Column(db.Integer, primary_key=True)
    tos=db.Column(db.Text, nullable=False)
    diarrea=db.Column(db.Text, nullable=False)
    tiene_sintomas=db.Column(db.Text, nullable=False)
    dolor_garganta=db.Column(db.Text, nullable=False)
    congestion_nasal=db.Column(db.Text, nullable=False)
    dificultad_respiratoria=db.Column(db.Text, nullable=False)
    fiebre_escalofrio=db.Column(db.Text, nullable=False)
    malestar_general=db.Column(db.Text, nullable=False)
    nauseas_vomito=db.Column(db.Text, nullable=False)
    cefalea=db.Column(db.Text, nullable=False)
    irritabilidad_confusion=db.Column(db.Text, nullable=False)
    otros=db.Column(db.Text, nullable=False)
    dolor_muscular=db.Column(db.Text, nullable=False)
    dolor_abdominal=db.Column(db.Text, nullable=False)
    dolor_pecho=db.Column(db.Text, nullable=False)
    dolor_articulaciones=db.Column(db.Text, nullable=False)

def format_sintomas(sintomas):
    return {
        "id": sintomas.id_sintomas,
        "tos": sintomas.tos,
        "diarrea": sintomas.diarrea,
        "tiene sintomas": sintomas.tiene_sintomas,
        "dolor de garganta": sintomas.dolor_garganta,
        "congestion nasal": sintomas.congestion_nasal,
        "dificultad_respirtoria": sintomas.dificultad_respiratoria,
        "fiebre y escalofrio": sintomas.fiebre_escalofrio,
        "malestar general": sintomas.malestar_general,
        "nauseas y vomito": sintomas.nauseas_vomito,
        "cefalea": sintomas.cefalea,
        "irritabildad y confusion": sintomas.irritabilidad_confusion,
        "otros": sintomas.otros,
        "dolor muscular": sintomas.dolor_muscular,
        "dolor abdominal": sintomas.dolor_abdominal,
        "dolor de pecho": sintomas.dolor_pecho,
        "dolor de articulaciones": sintomas.dolor_articulaciones
    }
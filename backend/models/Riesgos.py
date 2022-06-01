from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:pacris23@localhost/prototipo'
db=SQLAlchemy(app)

class Riesgos(db.Model):
    __tablename__="riesgos"
    id_riesgos=db.Column(db.Integer, primary_key=True)
    personal_salud=db.Column(db.Text, nullable=False)
    obesidad=db.Column(db.Text, nullable=False)
    enf_pulmonar_cronica=db.Column(db.Text, nullable=False)
    diabetes=db.Column(db.Text, nullable=False)
    hipertension_arterial=db.Column(db.Text, nullable=False)
    enf_tratinmuno=db.Column(db.Text, nullable=False)
    cancer=db.Column(db.Text, nullable=False)
    embarazo=db.Column(db.Text, nullable=False)
    mayor_60_años=db.Column(db.Text, nullable=False)
    ninguno=db.Column(db.Text, nullable=False)
    enf_cardiovascular=db.Column(db.Text, nullable=False)
    asma=db.Column(db.Text, nullable=False)

def format_riesgos(riesgos):
    return {
        "id": riesgos.id_riesgos,
        "personal de salud": riesgos.personal_salud,
        "obesidad": riesgos.obesidad,
        "enfermedad pulmonar": riesgos.enf_pulmonar_cronica,
        "diabetes": riesgos.diabetes,
        "hipertencion arteriañ": riesgos.hipertension_arterial,
        "enfermedad tratinmuno": riesgos.enf_tratinmuno,
        "cancer": riesgos.cancer,
        "embarazo": riesgos.embarazo,
        "mayor de 60 anios": riesgos.mayor_60_años,
        "ninguno": riesgos.ninguno,
        "enfermedad cardiovascular": riesgos.enf_cardiovascular,
        "asma": riesgos.asma
    }
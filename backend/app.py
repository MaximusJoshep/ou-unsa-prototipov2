#from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request
from models.Tiempo import*
from models.Persona import*
from models.Prueba import*
from models.Sintomas import*
from models.Riesgos import*


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/prototipo'
db=SQLAlchemy(app)

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__(self, description):
        self.description=description


def format_event(event):
    return{
        "description": event.description,
        "id": event.id,
        "created_at": event.created_at

    } 



@app.route('/')
def hello():
    return 'Hey!'


@app.route('/events', methods = ['POST'])
def create_event():
    description=request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

@app.route('/events', methods = ['GET'])
def get_events():
    events=Event.query.order_by(Event.id.asc()).all()
    event_list=[]
    for event in  events:
        event_list.append(format_event(event))  
    return {'Eventos':event_list}

@app.route('/events/<id>', methods = ['GET'])
def get_event(id):
    event=Event.query.filter_by(id=id).one()
    return {'Evento': format_event(event)}

@app.route('/events/<id>', methods = ['DELETE'])
def delete_event(id):
    event=Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Even (id: {id}) deleted!'

@app.route('/events/<id>', methods = ['PUT'])
def update_event(id):
    event= Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description,  created_at=datetime.utcnow()))
    db.session.commit()
    return {'Event': format_event(event.one())}


@app.route('/tiempos', methods = ['GET'])
def get_times():
    tiempos=Tiempo.query.order_by(Tiempo.id_tiempo.asc()).all()
    tiempo_list=[]
    for tiempo in  tiempos:
        tiempo_list.append(format_tiempo(tiempo))
    return {'Tiempos':tiempo_list}

@app.route('/tiempos/<id>', methods = ['GET'])
def get_time(id):
    tiempo=Tiempo.query.filter_by(id_tiempo=id).one()
    return {'Tiempo':format_tiempo(tiempo)}

@app.route('/personas', methods = ['GET'])
def get_people():
    personas=Persona.query.order_by(Persona.id_persona.asc()).all()
    persona_list=[]
    for persona in  personas:
        persona_list.append(format_persona(persona))
    return {'Personas':persona_list}

@app.route('/pruebas', methods = ['GET'])
def get_test():
    pruebas=Prueba.query.order_by(Prueba.id_prueba.asc()).all()
    prueba_list=[]
    for prueba in  pruebas:
        prueba_list.append(format_prueba(prueba))
    return {'Pruebas':prueba_list}

@app.route('/sintomas', methods = ['GET'])
def get_symptom():
    sintomas=Sintomas.query.order_by(Sintomas.id_sintomas.asc()).all()
    sintoma_list=[]
    for sintoma in  sintomas:
        sintoma_list.append(format_sintomas(sintoma))
    return {'Sintomas':sintoma_list}

@app.route('/riesgos', methods = ['GET'])
def get_risks():
    riesgos=Riesgos.query.order_by(Riesgos.id_riesgos.asc()).all()
    riesgo_list=[]
    for riesgo in  riesgos:
        riesgo_list.append(format_riesgos(riesgo))
    return {'Riesgos':riesgo_list}





if __name__=='__main__':
    app.run()
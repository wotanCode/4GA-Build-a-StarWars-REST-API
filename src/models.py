from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    #planet = db.Column(db.String(80), unique=False, nullable=False) recordar comentar porque se comento esta linea
    id_planet = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship ('Planet', lazy=True, uselist=True)
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "planets": self.planets
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    density = db.Column(db.String(80), unique=False, nullable=False)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "density": self.density,
            "id_people": self.id_people
            # do not serialize the password, its a security breach
        }
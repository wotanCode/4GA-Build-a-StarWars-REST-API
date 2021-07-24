from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritesVehicle = db.relationship ('FavoritesVehicle', lazy=True, uselist=False)

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
    name = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    #planet = db.Column(db.String(80), unique=False, nullable=False) recordar comentar porque se comento esta linea
    #GUARDANDO RELACIONES
    id_planet = db.Column(db.Integer, db.ForeignKey('planet.id'))
    #RELACIONES
    planet = db.relationship ('Planet', lazy=True, uselist=False)
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_planet": self.id_planet,
            #"planet": self.planet, esto serializa porque no se puede serializar una relacion
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    density = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    #id_people = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "density": self.density,
            "climate": self.climate,
            "gravity": self.gravity,
            #"id_people": self.id_people
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(80), unique=False, nullable=False)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    vehicle_class = db.Column(db.String(80), unique=False, nullable=False)
    favoritesVehicle = db.relationship ('FavoritesVehicle', lazy=True, uselist=False)
    #id_people = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "passengers": self.passengers,
            "vehicle_class": self.vehicle_class,
            #"id_people": self.id_people
            # do not serialize the password, its a security breach
        }

class FavoritesVehicle(db.Model):
    __tablename__ = 'favoritesVehicle'
    id = db.Column(db.Integer, primary_key=True)
    #GUARDANDO RELACIONES
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    #RELACIONES
    #user = db.relationship ('User', lazy=True, uselist=False)
    #vehicle = db.relationship ('Vehicle', lazy=True, uselist=False)
    #planet = db.relationship ('Planet', lazy=True, uselist=False)
    
    def __repr__(self):
        return '<FavoritesVehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            #"planet": self.planet, esto serializa porque no se puede serializar una relacion
            # do not serialize the password, its a security breach
        }
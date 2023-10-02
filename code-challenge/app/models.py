from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String)
    super_name = db.column(db.string)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    

class Power(db.Model, SerializerMixin):
    __tablename__ = 'power'

# Add validation
    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError("Description must be present.")
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description
    
    id = db.Column(db.Integer, primary_key=True) 
    name = db.column(db.string)
    description = db.column(db.string)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_power'   


    @validates('strength')
    def validate_strength(self, key, strength):
        allowed_strengths = ['Strong', 'Weak', 'Average']
        if strength not in allowed_strengths:
            raise ValueError("Strength must be one of 'Strong', 'Weak', 'Average'.")
        return strength

    id = db.column(db.Interger, primary_key=True)
    strength = db.column(db.string)
    hero_id = db.column(db.interger)
    power_id = db.column(db.Interger)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())






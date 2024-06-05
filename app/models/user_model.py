from werkzeug.security import generate_password_hash,check_password_hash
from app.database import db
from flask_login import UserMixin
import json

class User(UserMixin,db.Model):
    __tablename__="users"

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),unique=True, nullable=False)
    password_hash=db.Column(db.String(128),nullable=False)
    roles=db.Column(db.String(100),nullable=False)

    def __init__(self,username,password, roles=["user"]):
        self.username=username
        self.password_hash=generate_password_hash(password)
        self.roles=json.dumps(roles)

    def has_role(self,role):
        return self.role==role

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
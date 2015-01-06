from app import db
from app.users import constants as USER

from app.clients.models import Client


clients = db.Table('clients',
    db.Column('client_id', db.Integer, db.ForeignKey('clients_client.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users_user.id')),
)

class User(db.Model):

    __tablename__ = 'users_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    clients = db.relationship('Client', secondary=clients,
                              backref=db.backref('users_user', lazy='dynamic'))


    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def get_role(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)


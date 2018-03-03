'''
宣告資料表欄位
'''
import datetime

from .main import db

parents_homes = db.Table('parents_homes', db.Model.metadata,
    db.Column('parents_id', db.Integer, db.ForeignKey('parents.id')),
    db.Column('homes_id', db.Integer, db.ForeignKey('homes.id'))
)

class Parents(db.Model):
    # 可指定為其他的 database
    # __bind_key__ = 'otherDataBase'
    # 若不寫則看 class name
    __tablename__  = 'parents'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)

    childs = db.relationship("Childs", back_populates="parent", foreign_keys='Childs.parent_id')
    
    homes = db.relationship("Homes", secondary=parents_homes, back_populates="parents")
            
    def __repr__(self):
        return '<Parents {}>'.format(self.name)
        
        
class Childs(db.Model):
    # 若不寫則看 class name
    __tablename__  = 'childs'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'), nullable=False)
    parent = db.relationship("Parents", back_populates="childs", foreign_keys=[parent_id])
            
    def __repr__(self):
        return '<Childs {}>'.format(self.name)
        
        
class Homes(db.Model):
    # 若不寫則看 class name
    __tablename__  = 'homes'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    
    parents = db.relationship("Parents", secondary=parents_homes, back_populates="homes")
            
    def __repr__(self):
        return '<Childs {}>'.format(self.name)
        

# Create user model.
class Users(db.Model):
    # 若不寫則看 class name
    __tablename__  = 'users'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Users {}>'.format(self.name)
    
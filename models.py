"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS!

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<User {self.id} {self.first_name} {self.last_name} {self.image_url}>"

    def get_users():
      return User.query
    
    def get_user_by_id(id):
      user = User.query.get_or_404(id)
      return user
    
    def get_full_name(self):
       return f"{self.first_name} {self.last_name}"
    
    def add_users(firstname, lastname, imageurl=''):
      user = User(first_name=firstname, last_name=lastname, image_url=imageurl)
      db.session.add(user)
      db.session.commit()
      return True
    
    def update_users(id,firstname, lastname, imageurl=''):
      
      user = User.query.get_or_404(id)
      user.first_name=firstname
      user.last_name=lastname
      user.image_url=imageurl

      db.session.add(user)
      db.session.commit()
      return True
    
    def delete_users(id):
      user = User.query.get_or_404(id)
      db.session.delete(user)
      db.session.commit()
      return True
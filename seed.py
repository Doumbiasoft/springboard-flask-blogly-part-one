"""Seed file to make sample data for db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

User.query.delete()

# Add sample users
user2 = User(first_name='Denzel', last_name='Washington', image_url='https://m.media-amazon.com/images/I/61eAcaU-gGL._AC_SL1000_.jpg')
user3 = User(first_name='Kylian', last_name='Mbappé', image_url='https://www.sportsunfold.com/wp-content/uploads/2022/08/284095.jpg')
user1 = User(first_name='Mouhamed', last_name='Doumbia', image_url='')


db.session.add_all([user1, user2, user3])
db.session.commit()



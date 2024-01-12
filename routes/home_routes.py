
from flask import  render_template
from base import app, db
from models import Venue, Area, Artist, Show, Genre, Artist_Genre, Venue_Genre
from mock_data import seed_database

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/flush')
def flush_database():
    db.session.query(Show).delete()
    db.session.query(Venue_Genre).delete()
    db.session.query(Venue).delete()
    db.session.query(Artist_Genre).delete()
    db.session.query(Area).delete()
    db.session.query(Artist).delete()
    db.session.query(Genre).delete()

    db.session.commit()
    return 'Database flushed!'

@app.route('/seed/')
def seed():
    seed_database()
    return 'Database seeded!'
    


from flask import  render_template
from base import app, db
from models import Venue, Area, Artist, Show, Genre, Artist_Genre, Venue_Genre, Artist_Availability
from mock_data import seed_database

@app.route('/')
def index():
    recent_artists = Artist.query.order_by(Artist.id.desc()).limit(10).all()
    return render_template('pages/home.html', recent_artists=recent_artists)

@app.route('/flush/123')
def flush_database():
    db.session.query(Show).delete()
    db.session.query(Venue_Genre).delete()
    db.session.query(Venue).delete()
    db.session.query(Artist_Genre).delete()
    db.session.query(Area).delete()
    db.session.query(Artist_Availability).delete()
    db.session.query(Artist).delete()
    db.session.query(Genre).delete()

    db.session.commit()
    return render_template('pages/home.html')

@app.route('/seed/123')
def seed():
    seed_database()
    return render_template('pages/home.html')
    

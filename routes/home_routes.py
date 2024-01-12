
from flask import  render_template
from base import app, db
from models import Venue, Area, Artist, Show, Genre, Artist_Genre, Venue_Genre

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/flush')
def flush_database():
    db.session.query(Show,Area,Artist,Venue,Genre,Artist_Genre,Venue_Genre).delete()
  

    db.session.commit()
    return 'Database flushed!'

from flask import  render_template
from base import app, db
from models import Artist

@app.route('/')
def index():
    recent_artists = Artist.query.order_by(Artist.id.desc()).limit(10).all()
    return render_template('pages/home.html', recent_artists=recent_artists)



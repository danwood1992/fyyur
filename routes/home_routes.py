
from flask import  render_template
from base import app
from models import Venue

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/del_all_data/')
def del_all_data():
    venues=Venue.query.all()
  
    for venue in venues:
      venue.delete()

    return render_template('pages/home.html')

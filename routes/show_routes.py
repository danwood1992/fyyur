from flask import render_template, request, flash
from base import app
from models import Show, Artist
from forms import ShowForm

@app.route('/shows')
def shows():
  
    shows=Show.query.all()
    for show in shows:
      print(show.artist.name)
    return render_template('pages/shows.html', shows=shows)

@app.route('/shows/create')
def create_shows():
    # renders form. do not touch
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['GET'])
def create_show_form():
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)

@app.route('/shows/search', methods=['POST'])
def search_shows():
    search_term=request.form.get('search_term', '')

    artists = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()

    artist_shows = []

    for artist in artists:
        artist_shows += artist.shows

    response={
        "count": len(artist_shows),
        "data":  artist_shows
    }

    return render_template('pages/search_shows.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/shows/create', methods=['POST'])
def create_show_submission():

    form = ShowForm(request.form)
    show = Show(
      artist_id = form.artist_id.data,
      venue_id = form.venue_id.data,
      start_time = form.start_time.data,
    )

    success = show.create_show()
    if success:
        message = f'Show was successfully listed!'
        flash(message)
    else:
        message = f'Artist is not available at that time! Check their availability'
        flash(message)

    return render_template('pages/home.html')


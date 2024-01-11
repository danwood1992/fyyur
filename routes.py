
from flask import  render_template, request, flash, redirect, url_for
from base import app

from forms import *
from models import Venue, Artist, Show, Genre, Venue_Genre, Artist_Genre

@app.route('/')
def index():
  return render_template('pages/home.html')

@app.route('/venues')
def venues():
  venues = Venue.query.all()

  return render_template('pages/venues.html', areas=venues)

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm(

  )
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  
  form = VenueForm(request.form)
  venue = Venue(
    name = form.name.data,
    city = form.city.data,
    state = form.state.data,
    address = form.address.data,
    phone = form.phone.data,
    facebook_link = form.facebook_link.data,
    image_link = form.image_link.data, 
    website_link = form.website_link.data,
    seeking_talent = form.seeking_talent.data, 
    seeking_description = form.seeking_description.data,
    )
  venue.add()

  genre = Genre(name=form.genres.data)
  genre.add()
   
  venue_genre = Venue_Genre(venue=venue, genre=genre)
  venue_genre.add()

  if venue and venue_genre:

    flash('Venue ' + request.form['name'] + ' was successfully listed!')
   
    return render_template('pages/home.html')
  else:
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
    return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  venue = Venue.query.get(venue_id)
  venue.delete()
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

@app.route('/artists')
def artists():
  artists_data = Artist.query.all()

  return render_template('pages/artists.html', artists=artists_data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term=request.form.get('search_term', '')
  artists_data = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
  response={
    "count": len(artists_data),
    "data": artists_data
  }
 
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  data1 = Artist.query.get(artist_id)
  data2 = Artist_Genre.query.filter_by(artist_id=artist_id).all()
  data3 = Show.query.filter_by(artist_id=artist_id).all()
  data4 = Genre.query.filter_by(id=data2[0].genre_id).all()
  
  data = list(filter(lambda d: d['id'] == artist_id, [data1, data2, data3, data4]))[0]
  return render_template('pages/show_artist.html', artist=data)


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  artist = Artist.query.get(artist_id)
  artist_genres = Artist_Genre.query.filter_by(artist_id=artist_id).all()

  form = ArtistForm(
    name = artist.name,
    city = artist.city,
    state = artist.state,
    phone = artist.phone,
    facebook_link = artist.facebook_link,
    image_link = artist.image_link,
    website_link = artist.website_link,

    seeking_description = artist.seeking_description,
    genres = artist_genres

  )


  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  venue = Venue.query.get(venue_id)
  form = VenueForm()
  
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = ArtistForm(request.form)

  artist = Artist(
    name = form.name.data,
    city = form.city.data,
    state = form.state.data,
    phone = form.phone.data,
    facebook_link = form.facebook_link.data,
    image_link = form.image_link.data,
    website_link = form.website_link.data,
    seeking_venue = form.seeking_venue.data,
    seeking_description = form.seeking_description.data,
    )
  
  current_genres = Genre.query.all()
  for genre in form.genres.data:
    if genre not in current_genres:
      new_genre = Genre(name=genre)
      new_genre.add()

  artist_genre = Artist_Genre(artist=artist, genre=genre)

  artist_genre_success = artist_genre.add()
  artist_success = artist.add()

  if artist_genre_success and artist_success:
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  else:
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')

  
  return render_template('pages/home.html')

@app.route('/shows')
def shows():
  
  data=Show.query.all()
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['GET'])
def create_show_form():
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():

  form = ShowForm(request.form)
  show = Show(
    artist_id = form.artist_id.data,
    venue_id = form.venue_id.data,
    start_time = form.start_time.data,
  )
  show.add()

  
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/all_venues/')
def all_venues():
  venues=Venue.query.all()
  print(venues)
  return render_template('pages/all_data.html',venues=venues)

@app.route('/del_all_data/')
def del_all_data():
  venues=Venue.query.all()
  artists=Artist.query.all()
  shows=Show.query.all()
  genres=Genre.query.all()
  venue_genres=Venue_Genre.query.all()
  artist_genres=Artist_Genre.query.all()
  for artist_genre in artist_genres:
    artist_genre.delete()
  for venue_genre in venue_genres:
    venue_genre.delete()
  for genre in genres:
    genre.delete()
  for show in shows:
    show.delete()
  for artist in artists:
    artist.delete()
  for venue in venues:
    venue.delete()

  return render_template('pages/home.html')

from models import Venue, Venue_Genre, Genre, Area
from forms import VenueForm
from flask import render_template, request, flash, redirect, url_for
from base import app

@app.route('/venues')
def venues():
    venues = Venue.query.all()
    areas = Area.query.all()
    venue_genres = Venue_Genre.query.all()
    print(venue_genres)
    return render_template('pages/venues.html', venues=venues, areas=areas, genres = venue_genres)

@app.route('/venues/search', methods=['POST'])
def search_venues():
    search_term=request.form.get('search_term', '')
    venues_data = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).all()
    response={
        "count": len(venues_data),
        "data": venues_data
    }
 
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm(

  )
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  
  form = VenueForm(request.form)

  exisiting_area = Area.query.filter_by(city=form.city.data, state=form.state.data).first()

  if exisiting_area:
      area = exisiting_area
  else:
      area = Area(city=form.city.data, state=form.state.data)
      area.add()

  venue = Venue(
      name = form.name.data,
      address = form.address.data,
      phone = form.phone.data,
      facebook_link = form.facebook_link.data,
      image_link = form.image_link.data, 
      website_link = form.website_link.data,
      seeking_talent = form.seeking_talent.data, 
      seeking_description = form.seeking_description.data,
      area = area,
        )
 
  for genre in form.genres.data:
    print(f"genre: {genre}")
    if Genre.query.filter_by(name=genre).first():
      venue_genre = Venue_Genre(venue=venue, genre=Genre.query.filter_by(name=genre).first())
      venue_genre.add()
    else: 
      genre = Genre(name=genre)
      genre.add()
      venue_genre = Venue_Genre(venue=venue, genre=genre)
      venue_genre.add()

  if venue and venue_genre:

      flash('Venue ' + request.form['name'] + ' was successfully listed!')
      return render_template('pages/home.html')
  else:
      flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
      return render_template('pages/home.html')
  

@app.route('/venues/<venue_id>')
def show_venue(venue_id):
    venue = Venue.query.get(venue_id)
    print(f"venue: {venue}, {venue.past_shows}")

    return render_template('pages/show_venue.html', venue=venue)

@app.route('/all_venues/')
def all_venues():
    venues=Venue.query.all()
    print(venues)
    return render_template('pages/all_data.html',venues=venues)

@app.route('/venues/<venue_id>/delete', methods=['POST'])
def delete_venue(venue_id):
  venue = Venue.query.get(venue_id)
  print(f"deleting {venue}")
  venue.delete()

  return render_template('pages/home.html')

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = Venue.query.get(venue_id)
    genres = [genre.genre.name for genre in venue.genres]
    form = VenueForm(
      name = venue.name,
      address = venue.address,
      phone = venue.phone,
      facebook_link = venue.facebook_link,
      image_link = venue.image_link, 
      website_link = venue.website_link,
      seeking_talent = venue.seeking_talent, 
      seeking_description = venue.seeking_description,
      genres = genres,
      city = venue.area.city,
    )
    
    return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    venue = Venue.query.get(venue_id)
    form = VenueForm(request.form)

    
    return redirect(url_for('show_venue', venue_id=venue_id))



from models import Venue, Venue_Genre, Genre
from forms import VenueForm
from flask import render_template, request, flash, redirect, url_for
from base import app

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

@app.route('/all_venues/')
def all_venues():
    venues=Venue.query.all()
    print(venues)
    return render_template('pages/all_data.html',venues=venues)



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

def active_routes(active):
    if active:
        venues()
        create_venue_form()
        create_venue_submission()
        delete_venue()
        all_venues()
        edit_venue()
        edit_venue_submission()
        pass
    else:
        pass

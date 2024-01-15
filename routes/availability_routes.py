from flask import render_template, request, flash
from base import app
from models import Artist_Availability, Artist
from forms import AvailabilityForm


@app.route('/availability/create')
def create_availability():
  
    form = AvailabilityForm()
    return render_template('forms/new_availability.html', form=form)

@app.route('/availability/create', methods=['GET'])
def create_availabilty_form():
    form = AvailabilityForm()
    return render_template('forms/new_availability.html', form=form)


@app.route('/availability/create', methods=['POST'])
def create_availability_submission():

    form = AvailabilityForm(request.form)
    artist = Artist.query.get(form.artist_id.data)
    availability = Artist_Availability(
      artist = artist,
      start_time = form.start_time.data,
      end_time = form.end_time.data,
    )

    success = availability.add()
    if success:
      flash('Availabulty was successfully listed!')
    else:
      flash('An error occurred. Availabilty could not be listed.')

    return render_template('pages/home.html')



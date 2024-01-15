from base import app
from models import Artist, Genre, Artist_Genre, Show, Venue, Artist_Availability
from forms import ArtistForm
from flask import render_template, request, flash, redirect, url_for
import datetime

@app.route('/artists')
def artists():
    artists_data = Artist.query.all()

    return render_template('pages/artists.html', artists=artists_data)

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

            genre = Genre.query.filter_by(name=genre).first()

            artist_genre = Artist_Genre(artist=artist, genre=genre)
            artist_genre.add()

    artist_success = artist.add()

    if artist_success:
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
    else:
        flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')

    
    return render_template('pages/home.html')

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
    artist = Artist.query.get(artist_id)
    availabilities = Artist_Availability.query.filter_by(artist_id=artist_id).all()

    return render_template('pages/show_artist.html', artist=artist, availabilities=availabilities)


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

    artist = Artist.query.get(artist_id)
    form = ArtistForm(request.form)

    artist.name = form.name.data
    artist.city = form.city.data
    artist.state = form.state.data
    artist.phone = form.phone.data
    artist.facebook_link = form.facebook_link.data
    artist.image_link = form.image_link.data
    artist.website_link = form.website_link.data
    artist.seeking_venue = form.seeking_venue.data
    artist.seeking_description = form.seeking_description.data

    artist.update()

    return redirect(url_for('show_artist', artist_id=artist_id))

def active_routes(active):
    if active:
        artists()
        create_artist_form()
        create_artist_submission()
        search_artists()
        show_artist()
        edit_artist()
        edit_artist_submission()
        pass
    else:
        pass

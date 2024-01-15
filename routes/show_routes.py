from flask import render_template, request, flash
from base import app
from models import Show
from forms import ShowForm

@app.route('/shows')
def shows():
  
    shows=Show.query.all()
    for show in shows:
      print(show.artist.name)
    return render_template('pages/shows.html', shows=shows)

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

    success = show.add()
    if success:
      flash('Show was successfully listed!')
    else:
      flash('An error occurred. Show could not be listed.')

    return render_template('pages/home.html')


def active_routes(active):
    if active:
        shows()
        create_shows()
        create_show_form()
        create_show_submission()
        pass
    else:
        pass

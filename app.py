from base import app, db
import filters
import config
from datetime import datetime
from routes import availability_routes, venue_routes, artist_routes, show_routes, home_routes

SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(config)

if __name__ == '__main__':
    app.run(port=5025, debug=True)


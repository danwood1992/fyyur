from base import app, db
import routes, config

SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(config)

if __name__ == '__main__':
    app.run(port=5025, debug=True)


from base import app, db
import routes

SQLALCHEMY_TRACK_MODIFICATIONS = False

if __name__ == '__main__':
    app.run(port=5000, debug=True)


from base import app, db
import controllers

app.config.from_object('config')

if __name__ == '__main__':
    app.run(port=5050, debug=True, host='0.0.0.0')


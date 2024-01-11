from config import app

app.config.from_object('config')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')


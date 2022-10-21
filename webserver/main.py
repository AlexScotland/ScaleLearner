from flask import Flask
from webserver.blueprints.guitar import guitar_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(guitar_blueprint)

if __name__ == "__main__":
     app.run(host='0.0.0.0')
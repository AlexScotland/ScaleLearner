from flask import Flask
from webserver.blueprints.guitar import guitar_blueprint

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(guitar_blueprint)

if __name__ == "__main__":
    app.run()
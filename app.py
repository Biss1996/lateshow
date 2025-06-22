from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import all_routes



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/lateshow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(all_routes)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)
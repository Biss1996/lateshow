from flask import *
from .episodes import *
from .guests import *
from .appearances import *

all_routes = Blueprint('all_routes', __name__)
all_routes.register_blueprint(episodes_bp)
all_routes.register_blueprint(guests_bp)
all_routes.register_blueprint(appearances_bp)

from flask import Blueprint, request, jsonify
from models import db, Appearance

appearances_bp = Blueprint('appearances', __name__, url_prefix='/appearances')
from flask import Blueprint, request, jsonify
from models import db, Appearance, Guest, Episode

appearances_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearances_bp.route('', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        rating = data.get('rating')
        guest_id = data.get('guest_id')
        episode_id = data.get('episode_id')

        # check if guest and episode exist
        guest = Guest.query.get(guest_id)
        episode = Episode.query.get(episode_id)

        if not guest or not episode:
            return jsonify({"errors": ["validation errors"]}), 400

        # Validate rating value
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({"errors": ["Rating must be an integer between 1 and 5"]}), 400

        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()

        # Build full response as required
        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": guest.id,
            "episode_id": episode.id,
            "episode": episode.to_dict(),
            "guest": guest.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

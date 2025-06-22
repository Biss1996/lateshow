from flask import Blueprint, jsonify
from models import Episode

episodes_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episodes_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

@episodes_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    data = episode.to_dict()
    data['appearances'] = [
        {
            'id': ap.id,
            'rating': ap.rating,
            'guest_id': ap.guest_id,
            'episode_id': ap.episode_id,
            'guest': ap.guest.to_dict() if ap.guest else None
        } for ap in episode.appearances
    ]
    return jsonify(data)
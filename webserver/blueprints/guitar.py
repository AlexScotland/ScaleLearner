from flask import Blueprint, request
from webserver.instruments.api_guitar import APIGuitar
from src.theory.models import Note, Chord

guitar_blueprint = Blueprint('api', __name__, url_prefix='/api')

@guitar_blueprint.route('/guitar', methods=['GET'])
def guitar():
    guitar = APIGuitar()
    e = Note("E", 2)
    return guitar.get_all_note_positions_for_api(e)
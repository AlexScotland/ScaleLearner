from flask import Blueprint, request
from webserver.instruments.api_guitar import APIGuitar
from webserver.src.theory.models import Note, Chord

guitar_blueprint = Blueprint('api', __name__, url_prefix='/api')

@guitar_blueprint.route('/guitar/', methods=['GET'])
def guitar():
    note = request.args.get('note')
    if not note:
        return "Invalid Note Given"
    guitar = APIGuitar()
    e = Note(note.upper(), 2)
    return guitar.get_all_note_positions_for_api(e)
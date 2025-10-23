from flask import Blueprint

action_bp = Blueprint('accion', __name__)

@action_bp.route('/accion', methods=['GET'])
def get_acciones():
    return {"messeges": "Accion del ms uno"}, 200
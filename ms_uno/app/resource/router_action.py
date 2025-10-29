
from flask import Blueprint, jsonify


accion_bp = Blueprint('accion', __name__)

@accion_bp.route('/accion', methods=['POST'])
def accion():
    # Simula una acción exitosa
    print("MS UNO: Acción ejecutada")
    return jsonify({"message": "Acción ejecutada en ms_uno"}), 200


@accion_bp.route('/compensar', methods=['POST'])
def compensar():
    # Simula compensación
    print("MS UNO: Acción revertida (compensación)")
    return jsonify({"message": "Acción compensada en ms_uno"}), 200
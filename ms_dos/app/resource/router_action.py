from flask import Blueprint, request, jsonify

accion_bp = Blueprint('accion_dos', __name__)

@accion_bp.route('/accion', methods=['POST'])
def accion():
    data = request.get_json(force=True)
    if data.get("fail"):
        print("MS DOS: Error intencional durante la acción")
        return jsonify({"error": "Falla en ms_dos"}), 500

    print("MS DOS: Acción ejecutada correctamente")
    return jsonify({"message": "Acción ejecutada en ms_dos"}), 200


@accion_bp.route('/compensar', methods=['POST'])
def compensar():
    print("MS DOS: Acción revertida (compensación)")
    return jsonify({"message": "Acción compensada en ms_dos"}), 200

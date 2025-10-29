# saga_router.py
import logging
from saga import SagaBuilder, SagaError
from flask import jsonify, request,Blueprint
from app.services.saga_services import AccionesMicroservicios

logging.basicConfig(level=logging.INFO)

saga_bp = Blueprint('saga', __name__)

@saga_bp.route("/", methods=["POST"])
def ejecutar_saga():
    data = request.get_json(force=True)
    fail_dos = data.get("fail_dos", False)

    acciones = AccionesMicroservicios()
    exito = False

    try:
        SagaBuilder.create() \
            .action(lambda: acciones.accion_ms_uno(), lambda: acciones.compensar_ms_uno()) \
            .action(lambda: acciones.accion_ms_dos(fail_dos), lambda: acciones.compensar_ms_dos()) \
            .build().execute()
        
        exito = True

    except SagaError as err:
        for e in err.args:
            logging.error(f"SagaError: {e}")

    except Exception as e:
        logging.error(f"Error inesperado: {e}")

    return jsonify({"status": "OK" if exito else "ERROR"}), (200 if exito else 500)



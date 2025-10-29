import requests

# Endpoints de los microservicios
MS_UNO = "http://localhost:5001/ms_uno"
MS_DOS = "http://localhost:5002/ms_dos"

class AccionesMicroservicios:
    """Acciones y compensaciones para los microservicios"""

    def accion_ms_uno(self):
        r = requests.post(f"{MS_UNO}/accion")
        if r.status_code != 200:
            raise Exception("Fallo en acción ms_uno")

    def compensar_ms_uno(self):
        requests.post(f"{MS_UNO}/compensar")

    def accion_ms_dos(self, fail=False):
        r = requests.post(f"{MS_DOS}/accion", json={"fail": fail})
        if r.status_code != 200:
            raise Exception("Fallo en acción ms_dos")

    def compensar_ms_dos(self):
        requests.post(f"{MS_DOS}/compensar")
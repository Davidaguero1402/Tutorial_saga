import os
from dotenv import load_dotenv
import requests

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "LOCAL")

if ENVIRONMENT == "TRAEFIK":
    MS_UNO = os.getenv("MS_UNO_TRAEFIK")  # http://traefik
    MS_DOS = os.getenv("MS_DOS_TRAEFIK")  # http://traefik
else:
    MS_UNO = os.getenv("MS_UNO_LOCAL")    # http://localhost:5001/ms_uno
    MS_DOS = os.getenv("MS_DOS_LOCAL")    # http://localhost:5002/ms_dos

print(f"🧩 Modo: {ENVIRONMENT}")
print(f"MS_UNO = {MS_UNO}")
print(f"MS_DOS = {MS_DOS}")


class AccionesMicroservicios:
    def accion_ms_uno(self):
        r = requests.post(f"{MS_UNO}/accion")  # prefijo completo
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

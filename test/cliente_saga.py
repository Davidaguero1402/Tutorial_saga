import requests

url = "http://localhost:5000/saga/"

# --- Caso 1: Ejecución exitosa ---
print("---- SAGA EXITOSA ----")
data_ok = {"fail_dos": False}

response = requests.post(url, json=data_ok)

print(f"Status code: {response.status_code}")
print("Respuesta:", response.json())


# --- Caso 2: Ejecución fallida ---
print("\n---- SAGA CON FALLA EN MS_DOS ----")
data_fail = {"fail_dos": True}

response = requests.post(url, json=data_fail)

print(f"Status code: {response.status_code}")
print("Respuesta:", response.json())

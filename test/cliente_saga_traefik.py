import requests

url = "http://localhost/saga/"  # 👈 importante: el / final

print("---- SAGA EXITOSA ----")
data_ok = {"fail_dos": False}
response = requests.post(url, json=data_ok)
print("Status:", response.status_code)
print("Texto de respuesta:", repr(response.text))

print("\n---- SAGA FALLIDA ----")
data_fail = {"fail_dos": True}
response = requests.post(url, json=data_fail)
print("Status:", response.status_code)
print("Texto de respuesta:", repr(response.text))


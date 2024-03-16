import requests



# Función para obtener los diccionarios de la API
def leerApi(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al consultar la API. Código de estado:", response.status_code)
        return None




import requests

def obtener_datos():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Datos recibidos:", response.json())
    else:
        print("Error al conectar")

if __name__ == "__main__":
    obtener_datos()

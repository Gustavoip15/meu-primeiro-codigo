import requests
data = '2012-06-08'

resultado = requests.get('https://api.nasa.gov/planetary/apod?api_key=S7qoNMXgOKqGkk0csAmmWkNCp1TNfhNXOpWcEn9G&date={}'.format(data))
print(resultado.json())
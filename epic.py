import requests
data = '2012-06-08'

resultado = requests.get('https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=S7qoNMXgOKqGkk0csAmmWkNCp1TNfhNXOpWcEn9G&date={}'.format(data))
print(resultado.json())
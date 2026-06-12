import requests

# The URL points directly to an image asset
url = 'https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=S7qoNMXgOKqGkk0csAmmWkNCp1TNfhNXOpWcEn9G'
resultado = requests.get(url)

print(f"Status Code: {resultado.status_code}")

if resultado.status_code == 200:
    # Open a new file in 'wb' (write binary) mode and save the image content
    with open('nasa_earth.png', 'wb') as file:
        file.write(resultado.content)
    print("Image saved successfully as 'nasa_earth.png'!")
else:
    print("Failed to download the image.")
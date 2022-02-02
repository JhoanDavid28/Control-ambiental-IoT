import json
lista = {}
if __name__ == "__main__":
    with open('myDictionary.json') as file:
        data = json.load(file)

    def medicionesAlista():
        temperature = data['dic1']['variables']['temperature']
        humidity = data['dic1']['variables']['humidity']
        pollution = data['dic1']['variables']['contaminacion']
        return temperature, humidity, pollution

    lista['a'] = medicionesAlista()
    print(lista)




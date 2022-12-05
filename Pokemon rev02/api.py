import requests
import json
import random

global request 

def buscar():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/")
    todo = json.loads(request.content)
    print(todo)

def buscar_pokemon(nome):
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")

request = requests.get(f"https://pokeapi.co/api/v2/pokemon/")
todo = json.loads(request.content)   
status = {todo['stats'][0]['stat']['name'] ,todo['stats'][1]['stat']['name'],str(todo['stats'][1]['base_stat']),todo['stats'][2]['stat']['name'],str(todo['stats'][2]['base_stat']), todo['stats'][3]['stat']['name'],str(todo['stats'][3]['base_stat']), todo['stats'][4]['stat']['name'],str(todo['stats'][4]['base_stat']), todo['stats'][5]['stat']['name'],str(todo['stats'][5]['base_stat'])}
habilidades = {todo['abilities'][0]['ability']['name'],todo['abilities'][1]['ability']['name']}
tipo = {todo['id'],todo['types'][0]['type']['name'],todo['sprites']['front_default']}
nome = todo['name']
#print(str(nome) + " | " + str(status) + " | " + str(habilidades) + " | " + str(tipo))
    
   

if __name__ == '__main__':
    #buscar()
    lista_pokemon = ['pikachu', 'gengar', 'bulbasaur', 'dragonite','gyarados','charmander']
    indice_aleatorio = random.sample(lista_pokemon,1)
    api = buscar_pokemon(indice_aleatorio[0])
    print(habilidades)
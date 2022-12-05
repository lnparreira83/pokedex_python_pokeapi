import io
from pathlib import Path
import random
from tkinter import *
from tkinter import Tk, ttk 

from PIL import Image, ImageTk
from dados import *
import requests
import json
import random

#cores
co0 = "#444466" #Preta
co1 = "#feffff" #branca
co2 = "#6f9fbd" #azul
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#ef5350" #vermelha


#criando janela
janela = Tk()
janela.title('')
janela.geometry('650x610')
janela.configure(bg=co1)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemons = Frame(janela,width=650, height=300, relief='flat')
frame_pokemons.grid(row=1,column=0)

#funcao para trocar pokemon
def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem, api, validador_api, texto

    #trocando a cor do fundo do frame
    frame_pokemons['bg'] = pokemon[i]['tipo'][3]

    #tipo de pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    #api
    api = pok_nome['text'].lower()
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{api}")
    todo = json.loads(request.content)   

    if request.status_code == 200:
        validador_api = True

    else:
        validador_api = False
        pok_btn_pesquisa = Label(janela, text='Erro ao pesquisar pokemon',relief='flat',anchor=CENTER, font=('Verdana 12'), bg=co1, fg=co0)
        pok_btn_pesquisa.place(x=350,y=435)
        print('erro')

    #pokemon Habilidade
    if len(todo['abilities']) > 1:
        pok_habilidade1['text'] = todo['abilities'][0]['ability']['name'].upper()
        pok_habilidade2['text'] = todo['abilities'][1]['ability']['name'].upper()
    else:
        pok_habilidade1['text'] = todo['abilities'][0]['ability']['name'].upper()
        pok_habilidade2['text'] = ''
    
        
    
    #pokemon Status
    pok_hp['text'] = str(todo['stats'][0]['stat']['name']).upper() + ": " + str(todo['stats'][0]['base_stat'])
    pok_atack['text'] = str(todo['stats'][1]['stat']['name']).upper() + ": " + str(todo['stats'][1]['base_stat'])
    pok_defesa['text'] = str(todo['stats'][2]['stat']['name']).upper() + ": " + str(todo['stats'][2]['base_stat'])
    pok_velocidade['text'] = str(todo['stats'][3]['stat']['name']).upper() + ": " + str(todo['stats'][3]['base_stat'])
    pok_total['text'] = str(todo['stats'][4]['stat']['name']).upper() + ": " + str(todo['stats'][4]['base_stat'])

    #imagem do pokemon
    image = requests.get(todo['sprites']['other']['home']['front_default'])
    imagem_pokemon = Image.open(io.BytesIO(image.content))
    imagem_pokemon = imagem_pokemon.resize((210,210))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemons,image=imagem_pokemon,relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_imagem.place(x=230,y=50)

    pok_tipo.lift()


     

#nome
pok_nome = Label(frame_pokemons, text='',relief='flat',anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12,y=15)

#categoria
pok_tipo = Label(frame_pokemons, text='',relief='flat',anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12,y=50)

#id
pok_id = Label(frame_pokemons, text='',relief='flat',anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12,y=75)


#Status
pok_status = Label(janela, text='Status',relief='flat',anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15,y=350)

#hp
pok_hp = Label(janela, text='HP: 100',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15,y=390)

#Ataque
pok_atack = Label(janela, text='Ataque: 600',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15,y=430)

#defesa
pok_defesa = Label(janela, text='Defesa: 100',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15,y=470)

#velocidade
pok_velocidade = Label(janela, text='Velocidade: 100',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15,y=510)

#total
pok_total = Label(janela, text='Total: 100',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15,y=550)

#Habilidade
pok_habilidade = Label(janela, text='Habilidade',relief='flat',anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180,y=350)

#hp
pok_habilidade1 = Label(janela, text='',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_habilidade1.place(x=180,y=390)

#Ataque
pok_habilidade2 = Label(janela, text='',relief='flat',anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_habilidade2.place(x=180,y=430)

#Pesquisa
pok_pesquisa = Label(janela, text='Pesquisar pokemon',relief='flat',anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_pesquisa.place(x=350,y=350)

texto = Entry(janela)
texto.place(x=350,y=390)

pok_btn_pesquisa = Button(janela, text='Pesquisar pokemon',command= lambda:trocar_pokemon(texto.get()),relief='flat',anchor=CENTER, font=('Verdana 12'), bg=co1, fg=co0)
pok_btn_pesquisa.place(x=350,y=415)

def clearTextInput():
    texto.delete(0,END)

btnRead=Button(janela,text="x", 
                    command=clearTextInput)
btnRead.place(x=500,y=415)


lista_pokemon = ['Pikachu', 'Gengar', 'Bulbasaur', 'Dragonite','Gyarados','Charmander']
indice_aleatorio = random.sample(lista_pokemon,1)
trocar_pokemon(indice_aleatorio[0])

janela.mainloop()
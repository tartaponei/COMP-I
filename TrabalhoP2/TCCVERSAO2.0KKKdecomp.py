# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:16:48 2019

@author: CASA
"""
#teste

import sqlite3
import json

conexao = sqlite3.connect('elementos.db')
leitor = conexao.cursor()

def cadastra_elemento(nome, sigla, categoria, raio, configuracao_eletronica):
    leitor.execute("INSERT INTO elementos (nome, sigla, categoria, raio, configuracao_eletronica) VALUES(?,?,?,?,?)", (nome, sigla, categoria, raio, configuracao_eletronica))

def cria_tabela():
    tabela_periodica = json.load(open("PeriodicTableJSON.json"))["elements"] 
    for elemento in tabela_periodica:
        print(elemento["name"])
        cadastra_elemento(elemento["name"], elemento["symbol"], elemento["category"], 0, elemento["electron_configuration"])
        conexao.commit()
        
def aquitaos_elemento(sigla):
    return leitor.execute("SELECT * FROM elementos where upper(sigla) = '"+ sigla + "'").fetchall()[0]
    

print('Esse programa consiste em calcular a distancia entre as ligações do atomo central de uma molécula aos adjacentes')


def comparar_elementos():
    elemento1 = aquitaos_elemento(input('Digite um elemento').upper())
    elemento2 = aquitaos_elemento(input('Digite outro elemento').upper())
    if (elemento1[5] == "ametal" and elemento2[5] == "metal") or (elemento2[5] == "ametal" and elemento1[5] == "metal"):
        print('ligação ionica') 
        return "ionica"
    elif (elemento1[5] == "gas nobre" or elemento2[5] == "gas nobre"): 
        print('Inválido. Gases nobres já são estaveis por isso nao se associam com outros elementos')
        comparar_elementos()
    elif (elemento1[5] == "ametal" and elemento2[5] =="ametal"):
        print('ligação covalente')
        return "covalente"
tipoligacao = comparar_elementos()
#ta salvo na variavel ligação se é ionico ou covalente apartir dai segue:

#comparação vai servir pra saber que tipo de comando deve ser escrito ou executado a seguir tipo:
# comparou -> ametal + metal > comparar dnv agora o número de eletrons na camada de valencia > quem tiver o menor numero de eletrons
#vai ser o atomo central
#
#usar vetor para fazer comparação (?)
# transforma em vetor a camada eletronica elemento1[4].explode(" ")
#O calculo pra saber a quantidade de atomos ligantes

#A soma do raio do elemento 1 + a soma do raio do elemento 2 /(distancia media entre os núcleos de dois átomos ligados por uma ligação química)


    


#!/usr/bin/env  python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades
"""
__version__ = "0.1.0"

salas = {
        "sala1": ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"],
        "sala2": ["Joao","Antonio","Carlos","Maria", "Isolda"],
}

intersection = list[set(salas.items()) & set(atividades.items())]

atividades = {
        "aula_ingles": ["Erik","Maia","Joana","Carlos","Antonio"],
        "aula_musica":  ["Erik","Carlos","Maria"],
        "aula_dança":  ["Gustavo","Sofia","Joana","Antônio"],
}

for key, value in atividades.items():
     
        
    print(key," \n")
    print(intersection," \n")
    print(f"")
    print("-"*40)



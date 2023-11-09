#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotacaogeral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new", "search")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    #Leitura de notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag == arguments[1]:
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

if arguments[0] == "search":
   searchtext = arguments[1]
   with open(filepath, 'r') as file_:
       content = file_.read()
       for row in content:
           if row.find(searchtext) != -1:
                print('String exists')
                print('line Number:', lines.index(row))
                print('Line: ', line)

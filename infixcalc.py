#!/usr/bin/env python3
""" Prefix Calculator

"""
__version__ = "0.1.0"
__author__ = "Athos Camargo"
__license__ = "Unlicensed"

import sys
import os

from datetime import datetime

arguments = sys.argv[1:]

#TODO exceptions

if not arguments:
    operacao = input(f"operacao:")
    n1 = input(f"n1:")
    n2 = input(f"n2:")
    arguments= [operacao, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos invalidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

#desempacotar
operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", 'div')
if operation not in valid_operations:
    print("Operação Inválida")
    print(valid_operations)
    sys.exit(2)

validated_nums = []
for num in nums:
    if not num.isdigit():
        print(f"Numero invalido {num}")
        sys.exit(3)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

#desempacota
n1, n2 = validated_nums

# Todo: Usar dict funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")

print(f"o resultado é {result}")

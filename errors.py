#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to Ask Forgiveness than permission

try:
    raise RuntimeError("Ocoorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso")
finally:
    print("Execute isso sempre")

try:
    print(names[1])
except:
    print("Missing name in the list")
    sys.exit(1)

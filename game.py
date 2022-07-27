import os 
import random
from time import sleep
from types import NoneType

def run():
    words = read_file()
    intentos = 1

    # Seleccionamos una palabra aleatoria del archivo
    sel_word = words[random.randint(0,len(words)-1)]
    sel_word = sel_word.upper()
    my_word = [ sel_word[i]  for i in range(0,len(sel_word))] # Seccionamos los caracteres de la palabra en una lista
    found = [ False for i in range(0, len(my_word))] # Creamos una lista con la misma longitud de la palabra, cada elemento es false
    os.system('cls')
    while True:
        print(f'Intento: {intentos}')
        actives = game_print(my_word,found) 

        if actives == False:  # si no se encontro el caracter aumenta limpia la pantalla y aumenta el intento
            os.system('cls')
            intentos += 1
            continue
        elif actives == None: # si no se ingreso un caracter valido solo se limpia la pantalla
            os.system('cls')
            continue
        
        if found != actives: # si hay un valor distinto en la lista de encontrados a los valores anteriores se suma un intento sino no lo suma
            intentos += 1
            found = actives
        
        if False in found:    # busca si todavia quedan falsos en la lista de encontrados
            os.system('cls')
        else:
            os.system('cls')   # si no encuentra falsos todos son true y el juego termina
            print_actives(my_word,found)
            print('Has ganado el juego!')
            print(f'Intentos: {intentos}')
            break

def read_file():
    words = []
    with open('./data.txt','r', encoding='utf-8') as f:
        for line in f:
            if len(line.strip()) > 0:
                words.append(line.strip())
    return words

def game_print(word,actives):
    print('Adivina la palabra!')
    found = False
    print_actives(word,actives) # Imprimimos el juego

    charac = input('')
    
    if len(charac) != 1 or charac.isnumeric() or not charac.isalpha(): # si no se ingresa nada, es numerico o es una palabra se retorna false
        print('Debes ingresar una letra')
        sleep(2)
        return None
    for num, value in enumerate(word): # recorremos los caracteres de la palabra y si uno coincide con el ingresado cambiamos a true el indice en la lista de encontrados
        if value == charac.upper():
            actives[num] = True
            found = True
    
    if(found):  #Si se encontra al menos un caracter retornamos la lista de encontrados si no retornamos false
        return actives
    else:
        return False
    
def print_actives(word,actives): # Imprimimos letra por letra el ahorcado
    for num, value in enumerate(actives):
        if(value):
            print(word[num],end='')
        else:
            print('_',end='')
    print('')
    
    
if __name__ == '__main__':
    run()
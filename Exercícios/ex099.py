from time import sleep
def maior(* num):
    cont = maiorn = 0
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.4)
        if cont == 0:
            maiorn = n
        if n > maiorn:
            maiorn = n
        cont += 1
    print(f'\nForam computados {cont} números')
    print(f'O maior foi {maiorn}')

#Programa principal
maior(2, 3, 8, 9, 74)
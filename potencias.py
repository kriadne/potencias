
# exponente = 0
# while exponente <=100:
#     print(str(2**exponente))
#     exponente += 1

def run():
    exponente = 0
    num = int(input('numero a elevar: '))
    limite = int(input('limite: '))
    while int((num**exponente)) <= int(limite):
        print(f'{num} elevado a {exponente} es igual a {2**exponente}')
        exponente += 1

if __name__ == '__main__':
    run()
import getpass

password = str.lower(getpass.getpass('Ingrese un Password: '))
key=''
a=len(password)
inte=0
while key != password:
    if password.isalpha():
        print("Ok solo tiene letras del alfabeto (todas se pasan a minuscula)")
        for letra in password:
            inicio = ord('a')
            fin = ord('z') + 1
            d = inicio-1
            while d <= fin:
                d=d+1
                inte=1+inte
                if str(letra)==str(chr(d)):
                    key= key + letra 
                    break
    else:
        print("La Password tiene caracteres que NO son del alfabeto")
        password = str.lower(getpass.getpass('Ingrese un Password: '))
        a=len(password)

print(f"Su pass es {key} tiene {a} caracteres y la sacamos en {inte} intentos")
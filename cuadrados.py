def listnum(longitud):
    arraynum = []
    contador = 0
    while contador < longitud:
        contador += 1
        arraynum.append(contador)

    for a in arraynum:
        print(a*a)


if __name__ == '__main__':

    listnum(30)
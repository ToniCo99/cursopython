def listnum(longitud):

    squares = []
    for a in range(1, longitud + 1):
        if a%3 == 0:
            continue
        else:
            squares.append (a**2)



    print(squares)



if __name__ == '__main__':

    listnum(30)
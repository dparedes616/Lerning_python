def run():
    squeres = []
    for i in range(1, 101):
        if i % 3 !=0:
            squeres.append(i**2)
    print(squeres)
    print("-----------------------")

    squeres2 = [i**2 for i in range(0, 101) if i %3 !=0]
    print(squeres2)

    squeres3 = [i for i in range(0, 101) if i %4 ==0 and i %6 ==0 and i %9 ==0]
    print(squeres3)





if __name__ == "__main__":
    run()
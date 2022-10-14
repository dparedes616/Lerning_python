from numpy import square


def run():
    my_list = [1, 2, 3, 4, 5]
    square = [i**2 for i in my_list]
    print(square)

    square1 = list(map(lambda x: x**2, my_list))
    print(square)




if __name__ == "__main__":
    run()